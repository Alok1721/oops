#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

class Observer {
public:
    virtual void update(const string& message) = 0;
    virtual ~Observer() {}
};

class DriverInfo {
public:
    virtual string get_name() = 0;
    virtual string get_driver_type() = 0;
    virtual ~DriverInfo() {}
};

class DriverAvailability {
public:
    virtual bool is_available() = 0;
    virtual void set_availability(bool available) = 0;
    virtual ~DriverAvailability() {}
};

class RegularDriver : public DriverInfo, public DriverAvailability, public Observer {
public:
    string name;
    bool available_status;

    RegularDriver(string n) : name(n), available_status(true) {}
    string get_name() override { return "Regular Driver: " + name; }
    string get_driver_type() override { return "Regular"; }
    bool is_available() override { return available_status; }
    void set_availability(bool available) override { available_status = available; }
    void update(const string& message) override {
        cout << "Notification to " << get_name() << ": " << message << endl;
    }
};

class PremiumDriver : public DriverInfo, public DriverAvailability, public Observer {
public:
    string name;
    bool available_status;

    PremiumDriver(string n) : name(n), available_status(true) {}
    string get_name() override { return "Premium Driver: " + name; }
    string get_driver_type() override { return "Premium"; }
    bool is_available() override { return available_status; }
    void set_availability(bool available) override { available_status = available; }
    void update(const string& message) override {
        cout << "Notification to " << get_name() << ": " << message << endl;
    }
};

class Rider : public Observer {
public:
    string name;
    Rider(string n) : name(n) {}
    void update(const string& message) override {
        cout << "Notification to " << name << ": " << message << endl;
    }
};

class FareStrategy {
public:
    virtual double calculate_fare(double distance) = 0;
    virtual ~FareStrategy() {}
};

class StandardFare : public FareStrategy {
public:
    double calculate_fare(double distance) override { return distance * 1.5; }
};

class SurgeFare : public FareStrategy {
public:
    double calculate_fare(double distance) override { return distance * 3.5; }
};

class FareContext {
public:
    shared_ptr<FareStrategy> strategy;

    FareContext(const string& condition) {
        if (condition == "Surge") {
            strategy = make_shared<SurgeFare>();
        } else {
            strategy = make_shared<StandardFare>();
        }
    }

    double calculate_fare(double distance) {
        return strategy->calculate_fare(distance);
    }
};

class Ride {
public:
    virtual ~Ride() {}
    virtual int get_ride_id() = 0;
    virtual void book_ride(double dist, FareContext& fare_context) = 0;
    virtual void complete_ride() = 0;
    virtual void print_ride_details() = 0;
    virtual void add_horizon_line() = 0;
    virtual double get_fare() = 0;
};

class ConcreteRide : public Ride {
public:
    int ride_id;
    DriverInfo& driver_info;
    DriverAvailability& driver_availability;
    Rider& rider;
    string status;
    double distance;
    double fare;
    vector<Observer*> observers;

    ConcreteRide(int id, DriverInfo& di, DriverAvailability& da, Rider& r)
        : ride_id(id), driver_info(di), driver_availability(da), rider(r), status("Pending"), distance(0.0), fare(0.0) {
        observers.push_back(&r);
        if (auto* driver = dynamic_cast<Observer*>(&di)) {
            observers.push_back(driver);
        }
    }

    int get_ride_id() override { return ride_id; }

    void book_ride(double dist, FareContext& fare_context) override {
        if (driver_availability.is_available()) {
            distance = dist;
            fare = fare_context.calculate_fare(distance);
            status = "Booked";
            driver_availability.set_availability(false);
            cout << "Ride " << ride_id << " Booked Successfully" << endl;
            cout << rider.name << " is riding with " << driver_info.get_name() << endl;
            cout << "Fare: $" << fare << endl;
            cout << "Distance: " << distance << " km" << endl;
            cout << "Status: " << status << endl;
            notify_observers("Ride " + to_string(ride_id) + " booked.");
        } else {
            cout << "Driver " << driver_info.get_name() << " is not available" << endl;
        }
    }

    void complete_ride() override {
        if (status == "Booked") {
            status = "Completed";
            driver_availability.set_availability(true);
            cout << "Ride " << ride_id << " Completed Successfully" << endl;
            notify_observers("Ride " + to_string(ride_id) + " completed.");
        } else {
            cout << "Cannot complete ride " << ride_id << ", current status: " << status << endl;
        }
    }

    void print_ride_details() override {
        cout << "Ride " << ride_id << " Details:" << endl;
        cout << "Driver: " << driver_info.get_name() << endl;
        cout << "Rider: " << rider.name << endl;
        cout << "Status: " << status << endl;
        cout << "Distance: " << distance << " km" << endl;
    }

    void add_horizon_line() override {
        cout << "----------------------------------------" << endl;
    }

    double get_fare() override { return fare; }

private:
    void notify_observers(const string& message) {
        for (auto* observer : observers) {
            observer->update(message);
        }
    }
};

class RideDecorator : public Ride {
protected:
    shared_ptr<Ride> ride;

public:
    RideDecorator(shared_ptr<Ride> r) : ride(r) {}
    int get_ride_id() override { return ride->get_ride_id(); }
    void book_ride(double dist, FareContext& fare_context) override { ride->book_ride(dist, fare_context); }
    void complete_ride() override { ride->complete_ride(); }
    void print_ride_details() override { ride->print_ride_details(); }
    void add_horizon_line() override { ride->add_horizon_line(); }
    virtual double get_fare() override { return ride->get_fare(); }
};

class InsuranceDecorator : public RideDecorator {
public:
    InsuranceDecorator(shared_ptr<Ride> r) : RideDecorator(r) {}
    double get_fare() override {
        double base_fare = ride->get_fare();
        cout << "Adding $5 insurance fee to ride " << get_ride_id() << endl;
        return base_fare + 5.0;
    }
};

class ChildSeatDecorator : public RideDecorator {
public:
    ChildSeatDecorator(shared_ptr<Ride> r) : RideDecorator(r) {}
    double get_fare() override {
        double base_fare = ride->get_fare();
        cout << "Adding $3 child seat fee to ride " << get_ride_id() << endl;
        return base_fare + 3.0;
    }
};

class RideManager {
private:
    static RideManager* instance;
    vector<shared_ptr<Ride>> rides;
    int next_ride_id;

    RideManager() : next_ride_id(1) {}

public:
    static RideManager& get_instance() {
        if (!instance) {
            instance = new RideManager();
        }
        return *instance;
    }

    int add_ride(shared_ptr<Ride> ride) {
        rides.push_back(ride);
        return next_ride_id++;
    }

    void list_rides() {
        for (const auto& ride : rides) {
            ride->print_ride_details();
        }
    }
};

RideManager* RideManager::instance = nullptr;

class RideFactory {
public:
    static shared_ptr<Ride> create_ride(const string& ride_type, const string& driver_name, Rider& rider, bool add_insurance = false, bool add_child_seat = false) {
        int ride_id = RideManager::get_instance().add_ride(nullptr);
        shared_ptr<Ride> ride;
        if (ride_type == "Economy") {
            auto driver = make_shared<RegularDriver>(driver_name);
            ride = make_shared<ConcreteRide>(ride_id, *driver, *driver, rider);
        } else if (ride_type == "Premium") {
            auto driver = make_shared<PremiumDriver>(driver_name);
            ride = make_shared<ConcreteRide>(ride_id, *driver, *driver, rider);
        } else {
            throw runtime_error("Invalid ride type");
        }
        if (add_insurance) {
            ride = make_shared<InsuranceDecorator>(ride);
        }
        if (add_child_seat) {
            ride = make_shared<ChildSeatDecorator>(ride);
        }
        RideManager::get_instance().rides[ride_id - 1] = ride;
        return ride;
    }
};

int main() {
    Rider rider("Alice");
    FareContext standard_fare_context("Standard");
    FareContext surge_fare_context("Surge");

    auto ride1 = RideFactory::create_ride("Economy", "John Doe", rider, true, false);
    auto ride2 = RideFactory::create_ride("Premium", "Jane Smith", rider, false, true);

    ride1->add_horizon_line();
    ride1->book_ride(10.0, standard_fare_context);
    ride1->print_ride_details();
    cout << "Total Fare with Insurance: $" << ride1->get_fare() << endl;
    ride1->complete_ride();
    ride1->add_horizon_line();

    ride2->book_ride(15.0, surge_fare_context);
    ride2->print_ride_details();
    cout << "Total Fare with Child Seat: $" << ride2->get_fare() << endl;
    ride2->complete_ride();
    ride2->add_horizon_line();

    cout << "All Rides:" << endl;
    RideManager::get_instance().list_rides();

    return 0;
}