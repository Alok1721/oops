class Notification:
    def __init__(self):
        self.subscribers=[]

    def subscribe(self,user):
        self.subscribers.append(user)
    
    def notify(self,message):
        for user in self.subscribers:
            print(f"Notifications to {user.username}:{message}")