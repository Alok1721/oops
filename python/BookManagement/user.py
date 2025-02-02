class User:
    def __init__(self,username,password,role):
        self.username=username
        self.password=password
        self.role=role

class Admin(User):
    def __init__(self,username,password):
        super().__init__(username,password,"admin")
class Customer(User):
    def __init__(self,username,password):
        super().__init__(username,password,"customer")
class UserFactory:
    def __init__(self):
        self.users={} #Store registered users
    
    def register_user(self,username,password,role):
        if role=="admin":
            self.users[username]=Admin(username,password)
                    
        elif role=="customer":
            self.users[username]=Customer(username,password)
            
        else:
            raise ValueError("Invalid role!")
    def login_user(self,username,password):
        user=self.users.get(username)
        if user and user.password == password:
            return user
        return None
    