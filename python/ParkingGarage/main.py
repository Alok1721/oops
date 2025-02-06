import tkinter as tk
from tkinter import messagebox
from user import UserManager,create_user


class ParkingGarageApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Parking Garage System")
        self.root.geometry("400x400")

        self.user_manager=UserManager()

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.root, text="Parking Garage System", font=("Arial", 16))
        self.label_title.pack(pady=10)
        self.register_button = tk.Button(self.root, text="Register User", command=self.show_register_form)
        self.register_button.pack(pady=10)
        self.login_button = tk.Button(self.root, text="Login", command=self.show_login_form)
        self.login_button.pack(pady=10)
        self.display_button = tk.Button(self.root, text="Display All Users", command=self.display_users)
        self.display_button.pack(pady=10)

    def show_register_form(self):
        self.clear_widgets()
    
        self.label_register = tk.Label(self.root, text="Register User", font=("Arial", 14))
        self.label_register.pack(pady=10)
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()
        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()
        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()
        self.label_phone = tk.Label(self.root, text="Phone Number:")
        self.label_phone.pack()
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.pack()
        self.label_role = tk.Label(self.root, text="Role (e.g., Customer, Admin):")
        self.label_role.pack()
        self.entry_role = tk.Entry(self.root)
        self.entry_role.pack()

        self.label_user_id = tk.Label(self.root, text="User ID:")
        self.label_user_id.pack()
        self.entry_user_id = tk.Entry(self.root)
        self.entry_user_id.pack()

        self.submit_button = tk.Button(self.root, text="Register", command=self.register_user)
        self.submit_button.pack(pady=10)
        self.back_button = tk.Button(self.root, text="Back", command=self.back_to_menu)
        self.back_button.pack(pady=10)

    def show_login_form(self):
        self.clear_widgets()

        # Create login form widgets
        self.label_login = tk.Label(self.root, text="Login", font=("Arial", 14))
        self.label_login.pack(pady=10)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login_user)
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.back_to_menu)
        self.back_button.pack(pady=10)
    def display_users(self):
        users_list = self.user_manager.display_users()
        self.clear_widgets()
        self.label_users = tk.Label(self.root, text="All Registered Users", font=("Arial", 14))
        self.label_users.pack(pady=10)
        self.text_users = tk.Label(self.root, text=users_list, font=("Arial", 10), justify="left")
        self.text_users.pack()

        self.back_button = tk.Button(self.root, text="Back", command=self.back_to_menu)
        self.back_button.pack(pady=10)

    def register_user(self):
        try:
            user_id = int(self.entry_user_id.get())
            user_name = self.entry_name.get()
            email = self.entry_email.get()
            password = self.entry_password.get()
            phone_number = self.entry_phone.get()
            role = self.entry_role.get()

            user = create_user(user_id, user_name, email, password, phone_number, role)
            message = self.user_manager.register(user)

            messagebox.showinfo("Registration", message)

            self.back_to_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid input.")
    
    def login_user(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        message = self.user_manager.login(email, password)
        messagebox.showinfo("Login", message)

        if "logged in" in message:
            self.back_to_menu()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def back_to_menu(self):
        self.clear_widgets()
        self.create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingGarageApp(root)
    root.mainloop()