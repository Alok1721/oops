import time

class FixedWindowRateLimiter:
    def __init__(self,max_requests,window_size):
        self.max_requests=max_requests
        self.window_size=window_size
        self.request_counts={}
        self.start_times={}


    def allow_request(self,user_id):
        current_time=time.time()

        if user_id not in self.request_counts:
            self.request_counts[user_id]=0
            self.start_times[user_id]=current_time
        
        if current_time-self.start_times[user_id]>self.window_size:
            self.request_counts[user_id]=0
            self.start_times[user_id]=current_time
        if self.request_counts[user_id]<self.max_requests:
            self.request_counts[user_id]+=1
            return True
        return False
limiter=FixedWindowRateLimiter(5,10)

for i in range(20):
    if limiter.allow_request("user1"):
        print(f"request {i+1} allowed")
    else:
        print(f"request {i+1} blocked")
    time.sleep(1)
