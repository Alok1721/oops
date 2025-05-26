#Driver class for manage list of deliveries
#Delivery class for startTime, endTime, and deliveryId
#DeliveryService class for add, remove, and get deliveries


class Delivery:
    def __init__(self,startTime,endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.cost=endTime-startTime

class Driver:
    def __init__(self,driverId):
        self.driverId = driverId
        self.deliveries = []

    def addDelivery(self,startTime,endTime):
        delivery = Delivery(startTime,endTime)
        self.deliveries.append(delivery)
        return delivery.cost

class DeliveryService:
    def __init__(self):
        self.drivers = {}
        self.totalCost = 0
    def addDriver(self,driverId):
        if driverId not in self.drivers:
            self.drivers[driverId] = Driver(driverId)
        
    def addDelivery(self,driverId,startTime,endTime):
        if driverId not in self.drivers:
            self.addDriver(driverId)
        cost=self.drivers[driverId].addDelivery(startTime,endTime)
        self.totalCost +=cost