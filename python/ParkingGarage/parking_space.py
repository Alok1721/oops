class ParkingSpace:
    def __init__(self,space_id,location,space_type,is_available,price_per_hour):
        self.space_id=space_id
        self.location=location
        self.space_type=space_type
        self.is_available=is_available
        self.price_per_hour=price_per_hour

    def mark_unavailable(self):
        self.is_available=False


class ParkingLot:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.spaces=[]

        return cls._instance
    
    def add_space(self,space):
        self.spaces.append(space)

    def check_availability(self):
        return [space for space in self.spaces if space.is_available]
    