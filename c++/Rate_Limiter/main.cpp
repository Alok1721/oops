#include <unordered_map>
#include <memory>
#include <mutex>
#include <string>
#include <iostream>
#include <chrono>
#include <queue>
#include <vector>

using namespace std;

//createing the interface for rate limiting strategies
class IRateLimiterStrategy {
public:
    virtual ~IRateLimiterStrategy()=default;
    virtual bool allow_request()=0;
    virtual size_t current_count()=0;

};

//base ratelimiter class
class Ratelimiter{
    private:
        unique_ptr<IRateLimiterStrategy> strategy;
        
    public:
        RateLimiter(unique_ptr<IRateLimiterStrategy> strategy) : strategy(move(strategy)) {}
        bool allow_request() {
            return strategy->allow_request();
        }
        size_t current_count() {
            return strategy->current_count();
        }
};

//token bucket strategy implementation
class TokenBucketStrategy : public IRateLimiterStrategy {
private:
    mutex mtx;
    size_t tokens;
    size_t max_tokens;
    double rate_per_ms;
    chrono::steady_clock::time_point last_refill_time;

    void refill(){
        auto now=chrono::steady_clock::now();
        auto ms=chrono::duration<double,milli>(now-last_refill_time).count();
        tokens=min(max_tokens,tokens+static_cast<size_t>(ms*rate_per_ms));
        last_refill_time=now;
    }

public:
    TokenBucketStrategy(size_t max_tokens, double rate_per_second)
        : tokens(max_tokens), max_tokens(max_tokens), rate_per_ms(rate_per_second / 1000.0),
          last_refill_time(chrono::steady_clock::now()) {}

    bool allow_request() override {
        lock_guard<mutex> lock(mtx);
        refill();
        if (tokens > 0) {
            --tokens;
            return true;
        }
        return false;
    }

    size_t current_count() override {
        lock_guard<mutex> lock(mtx);
        refill();
        return tokens;
    }
};

//manager to handle clients and their rate limiters
class RateLimiterManager{

private:
    struct ClientData{
        unique_ptr<RateLimiter> rate_limiter;
        string strategy_type;

    }
    unordered_map<string, ClientData> clients;
    mutex mtx;
}
public:
    void register_client(const string& client_id,string& strategy_type,size_t max_requests,chrono::milliseconds window_or_rate)
    {
        lock_guard<mutex> lock(mtx);

        if(client.find(client_id)!=clients.end()){
            return false;
        }
        unique_ptr<IRateLimiterStrategy> strategy;
        if(strategy_type == "token_bucket") {
            strategy = make_unique<TokenBucketStrategy>(max_requests, window_or_rate.count());
        } else {
            cerr << "Unknown strategy type: " << strategy_type << endl;
            return false;
        }

        clients[client_id] = {make_unique<RateLimiter>(move(strategy)), strategy_type};
        return true;
    }
        bool allow_client_count(string &client_id)
        {
            lock_guard<mutex> lock(mtx);
            auto it = clients.find(client_id);
            if (it == clients.end()) {
                cerr << "Client not found: " << client_id << endl;
                return false;
            }
            return it->second.rate_limiter->allow_request();


        }

        size_t get_client_count(string & client_id)
        {
            lock_guard<mutex> lock(mtx);
            auto it = clients.find(client_id);
            if (it == clients.end()) {
                cerr << "Client not found: " << client_id << endl;
                return 0;
            }
            return it->second.rate_limiter->current_count();
        }

        bool update_client_strategy(const string&,client_id,string strategy_type,size_t max_requests,chrono::milliseconds,window_or_rate)
        {
            return register_client(client_id, strategy_type, max_requests, window_or_rate);
        }

        bool remove_client(const string& client_id) {
            lock_guard<mutex> lock(mtx);
            return clients.erase(client_id) > 0;
        }
    };

int main() {
    RateLimiterManager manager;
    string client_id = "client1";
    string strategy_type = "token_bucket";
    size_t max_requests = 10;
    chrono::milliseconds window_or_rate(1000); // 1 second
    if (manager.register_client(client_id, strategy_type, max_requests, window_or_rate)) {
        cout << "Client registered successfully." << endl;
    } else {
        cout << "Failed to register client." << endl;
    }
    for (int i = 0; i < 15; ++i) {
        if (manager.allow_client_count(client_id)) {
            cout << "Request " << i + 1 << " allowed." << endl;
        } else {
            cout << "Request " << i + 1 << " denied." << endl;
        }
        cout << "Current count: " << manager.get_client_count(client_id) << endl;
        this_thread::sleep_for(chrono::milliseconds(100)); // Simulate time between requests
    }
    return 0;
}