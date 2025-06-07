#include <iostream>
#include <string>
using namespace std;

class DriverInfo {
public:
    virtual string get_name() = 0;
    virtual string get_driver_type() = 0;
    virtual ~DriverInfo() {};
};

class DriverAvailability {
public:
    virtual bool is_available() = 0;
    virtual void set_availability(bool available) = 0;
    virtual ~DriverAvailability() {};
};

class RegularDriver : public DriverInfo, public DriverAvailability {
public:
    string name;
    bool available_status;

    RegularDriver(string n) : name(n), available_status(true) {}

    string get_name() override {
        return "Regular Driver: " + name;
    }

    string get_driver_type() override {
        return "Regular";
    }

    bool is_available() override {
        return available_status;
    }

    void set_availability(bool available) override {
        available_status = available;
    }
};

class PremiumDriver : public DriverInfo, public DriverAvailability {
public:
    string name;
    bool available_status;

    PremiumDriver(string n) : name(n), available_status(true) {}

    string get_name() override {
        return "Premium Driver: " + name;
    }

    string get_driver_type() override {
        return "Premium";
    }

    bool is_available() override {
        return available_status;
    }

    void set_availability(bool available) override {
        available_status = available;
    }
};

class Rider {
public:
    string name;
    Rider(string n) : name(n) {}
};

class FareStrategy {
public:
    virtual double calculate_fare(double distance) = 0;
    virtual ~FareStrategy() {};
};

class StandardFare : public FareStrategy {
public:
    double calculate_fare(double distance) override {
        return distance * 1.5;
    }
};

class SurgeFare : public FareStrategy {
public:
    double calculate_fare(double distance) override {
        return distance * 3.5;
    }
};

class Ride {
public:
    DriverInfo &driver_info;
    DriverAvailability &driver_availability;
    Rider &rider;
    string status;
    double distance;
    double fare;

    Ride(DriverInfo &di, DriverAvailability &da, Rider &r)
        : driver_info(di), driver_availability(da), rider(r),
          status("Pending"), distance(0.0), fare(0.0) {}

    void book_ride(double dist, FareStrategy &strategy) {
        if (driver_availability.is_available()) {
            distance = dist;
            fare = strategy.calculate_fare(distance);
            status = "Booked";
            driver_availability.set_availability(false);

            cout << "Ride Booked Successfully" << endl;
            cout << rider.name << " is riding with " << driver_info.get_name() << endl;
            cout << "Fare: $" << fare << endl;
            cout << "Distance: " << distance << " km" << endl;
            cout << "Status: " << status << endl;
        } else {
            cout << "Driver " << driver_info.get_name() << " is not available" << endl;
        }
    }

    void complete_ride() {
        if (status == "Booked") {
            status = "Completed";
            driver_availability.set_availability(true);
            cout << "Ride Completed Successfully" << endl;
        } else {
            cout << "Cannot complete ride, current status: " << status << endl;
        }
    }

    void print_ride_details() {
        cout << "Ride Details:" << endl;
        cout << "Driver: " << driver_info.get_name() << endl;
        cout << "Rider: " << rider.name << endl;
        cout << "Status: " << status << endl;
        cout << "Distance: " << distance << " km" << endl;
    }

    void add_horizon_line() {
        cout << "----------------------------------------" << endl;
    }
};

int main() {
    RegularDriver regularDriver("John Doe");
    PremiumDriver premiumDriver("Jane Smith");
    Rider rider("Alice");

    StandardFare standardFare;
    SurgeFare surgeFare;

    Ride ride1(regularDriver, regularDriver, rider);
    Ride ride2(premiumDriver, premiumDriver, rider);

    ride1.add_horizon_line();
    ride1.book_ride(10.0, standardFare);
    ride1.print_ride_details();
    ride1.complete_ride();
    ride1.add_horizon_line();

    ride2.book_ride(15.0, surgeFare);
    ride2.print_ride_details();
    ride2.complete_ride();
    ride2.add_horizon_line();

    return 0;
}
