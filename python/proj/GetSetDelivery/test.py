from ps1 import DeliveryService

ds= DeliveryService()

#add drivers
ds.addDriver("alok")
ds.addDriver("sachin")

#add deliverries
ds.addDelivery("alok",1,5)
ds.addDelivery("alok",6,10)
ds.addDelivery("sachin",2,4)
ds.addDelivery("sachin",3,7)

print("Total cost of deliveries:", ds.totalCost)
print("Deliveries for alok:")
for delivery in ds.drivers["alok"].deliveries:
    print(f"Start: {delivery.startTime}, End:{delivery.endTime},cost:{delivery.cost}")
print("Deliveries for sachin:")
for delivery in ds.drivers["sachin"].deliveries:
    print(f"Start: {delivery.startTime}, End:{delivery.endTime},cost:{delivery.cost}")