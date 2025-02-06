class Reservation:
    def __init__(self,reservation_id,user_id,space_id,start_time,end_time,total_cost):
        self.reservation_id=reservation_id
        self.user_id=user_id
        self.space_id=space_id
        self.start_time=start_time
        self.end_time=end_time
        self.total_cost=total_cost

    def calculate_cost(self):
        pass

    