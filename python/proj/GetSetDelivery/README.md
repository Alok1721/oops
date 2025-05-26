# 🚚 Driver Delivery Cost Management System (Rippling)
--efficient implementation of a delivery tracking system for managing drivers and their delivery schedules. The system is designed to calculate and return the total cost of all deliveries in an optimized manner.

## Problem Statement 1:
Design a system to manage drivers and their delivery schedules, calculating the total cost of all deliveries. The system should support the following functionalities:

### ✅ Functional Requirements
1. **addDriver(driverId)**: 
-Add a driver with a unique driverId to the system.
2. **addDelivery(driverId, startTime, endTime)**: -Assign a delivery to a driver with the given driverId, 
-specifying the startTime and endTime of the delivery. Assume the cost of a delivery is proportional to its duration (e.g., endTime - startTime).

3.**getTotalCost()**: 
-Return the total cost of all deliveries across all drivers in an optimized manner.

The cost should be computed efficiently, ideally by updating the total cost incrementally when deliveries are added, rather than recalculating it each time getTotalCost() is called.

---

## Problem Statement:2
--follow_up:
**1.PayUptoTime(upToTime)**:settle the cost of all deliveries that end on or before the upToTime.and return the total cost settled.
**2.getCostToPaid**: return total cost of deliveries that have not settled