# **1.PayUptoTime(upToTime)**:settle the cost of all deliveries that end on or before the upToTime.and return the total cost settled.
# **2.getCostToPaid**: return total cost of deliveries that have not settled

from ps1 import DeliveryService, Driver, Delivery

class ExtendedDeliveryService(DeliveryService):
    def __init__(self):
        super().__init__()
        self.settled_cost = 0
    
    def payUptoTime(self, upToTime):
        for driver in self.drivers.values():
            for delivery in driver.deliveries:
                if delivery.endTime<=upToTime:
                    self.settled_cost +=delivery.cost
                    delivery.endTime=float('inf')

    def getCostToBePaid(self):
        return self.totalCost-self.settled_cost
    