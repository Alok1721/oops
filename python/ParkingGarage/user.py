class User:
    def __init__(self,user_id,user_name,email,password,phone_number,role):
        self.user_id=user_id
        self.name=user_name
        self.email=email
        self.password=password
        self.phone_number=phone_number
        self.role=role
    def _repr_(self):
        return f"User{self.user_id},{self.name},{self.email},{self.role}"

class UserManager:
    def __init__(self):
        self.users={}

    def register(self,user):
        if user.email in self.users:
            return f"User with email {user.email} already exists."
        else:
            self.users[user.email] = user 
            return f"User {user.name} registered successfully with email {user.email}."

    def login(self,email,password):
        if email not in self.users:
            return f"User with email {email} not found."
        user=self.users[email]
        if user.password==password:
            return f"User {user.name} logged in successfully."
        else:
            return "Incorrect passwored"
    def display_users(self):
        if not self.users:
            return "No users registered."
        return "\n".join(str(user) for user in self.users.values())
def create_user(user_id,user_name,email,password,phone_number,role):
    return User(user_id,user_name,email,password,phone_number,role)

