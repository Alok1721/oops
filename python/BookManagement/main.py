from user import UserFactory
from catalog import Catalog
from book import Book
import tkinter as tk
from tkinter import messagebox



class BookStoreApp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x400")
        self.root.title("Online Bookstore")
        self.user_factory=UserFactory()
        self.catalog_obj=Catalog()
        self.main_screen()


    def main_screen(self):
        """Main Menu"""

        self.clear_screen()
        tk.Label(self.root,text="Online BookStore",font=("Arial",16,"bold")).pack(pady=10)
        tk.Button(self.root,text="Register",command=self.register_screen,width=15).pack(pady=5)
        tk.Button(self.root,text="login",command=self.login_screen,width=15).pack(pady=5)
        tk.Button(self.root,text="Exit",command=self.login_screen,width=15).pack(pady=5)
        
    def register_screen(self):
        """user Registration Window"""
        self.clear_screen()
        tk.Label(self.root,text="Register",font=("Arial",16,"bold")).pack(pady=10)
        tk.Label(self.root,text="Username:").pack()
        username_entry=tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root,text="Password:").pack()
        password_entry=tk.Entry(self.root,show="*")
        password_entry.pack()

        tk.Label(self.root,text="Role (admin/customer):").pack()
        role_entry=tk.Entry(self.root)
        role_entry.pack()

        def register():
            username=username_entry.get()
            password=password_entry.get()
            role=role_entry.get()

            if role in ["admin" , "customer"]:
                self.user_factory.register_user(username,password,role)
                messagebox.showinfo("Success","Registration Successful!!")
            else:
                messagebox.showerror("Error","Invalid role! choose 'admin' or 'customer'")

        tk.Button(self.root,text="Register",command=register,width=15).pack(pady=5)
        tk.Button(self.root,text="Back",command=self.main_screen,width=15).pack(pady=5)
        
    def login_screen(self):
        """user Login Window"""
        self.clear_screen()
        tk.Label(self.root,text="Login",font=("Arial",16,"bold")).pack(pady=10)
        tk.Label(self.root,text="Username:").pack()
        username_entry=tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root,text="Password:").pack()
        password_entry=tk.Entry(self.root,show="*")
        password_entry.pack()

        def login():
            username=username_entry.get()
            password=password_entry.get()
            user=self.user_factory.login_user(username,password)

            if user:
                messagebox.showinfo("Welcome",f"Loggine in as {user.role}")
                if user.role=="admin":
                    self.admin_panel()
                elif user.role=="customer":
                    self.customer_panel()
            else:
                messagebox.showerror("Error","Invalid credentials")
        tk.Button(self.root,text="Login",command=login,width=15).pack(pady=5)
        tk.Button(self.root,text="Back",command=self.main_screen,width=15).pack(pady=5)

    def admin_panel(self):
        """Admin Panel"""
        self.clear_screen()
        tk.Label(self.root,text="Admin Panel",font=("Arial",14,"bold")).pack(pady=10)
        tk.Button(self.root,text="Add book",command=self.add_book_screen,width=15).pack(pady=5)
        tk.Button(self.root,text="Remove book",command=self.remove_book_screen,width=15).pack(pady=5)
        tk.Button(self.root,text="List Books",command=self.list_books,width=15).pack(pady=5)
        tk.Button(self.root,text="Logout",command=self.main_screen,width=15).pack(pady=5)

    def add_book_screen(self):
        """Admin:Add a Book"""
        self.clear_screen()

        tk.Label(self.root,text="Add book",font=("Arial",14,"bold")).pack(pady=10)
        tk.Label(self.root,text="Title:").pack()
        title_entry=tk.Entry(self.root)
        title_entry.pack()

        tk.Label(self.root,text="Author:").pack()
        author_entry=tk.Entry(self.root)
        author_entry.pack()
        tk.Label(self.root,text="Genre:").pack()
        genre_entry=tk.Entry(self.root)
        genre_entry.pack()

        tk.Label(self.root,text="Price:").pack()
        price_entry=tk.Entry(self.root)
        price_entry.pack()


        def add_book():
            title=title_entry.get()
            author=author_entry.get()
            genre=genre_entry.get()


            try:
                price=float(price_entry.get())
                book=Book(title,author,genre,price)
                self.catalog_obj.add_book(book)
                messagebox.showinfo("Success","Book added successfully!")
                self.admin_panel()
            except ValueError:
                messagebox.showerror("Error","Invalid price!")
            
        tk.Button(self.root,text="Add",command=add_book,width=15).pack(pady=5)
        tk.Button(self.root,text="Back",command=self.admin_panel,width=15).pack(pady=5)

    def remove_book_screen(self):
        """Admin:Remove a Book"""
        self.clear_screen()
        tk.Label(self.root,text="Remove Book",font=("Arial",14,"bold")).pack(pady=10)
        tk.Label(self.root,text="Enter Title:").pack()
        title_entry=tk.Entry(self.root)
        title_entry.pack()

        def remove_book():
            title=title_entry.get()

            self.catalog_obj.remove_book(title)
            messagebox.showinfo("Success",f"Book {title} remove successfully")
            self.admin_panel()

        tk.Button(self.root,text="Remove",command=remove_book,width=15).pack(pady=5)
        tk.Button(self.root,text="Back",command=self.admin_panel,width=15).pack(pady=5)
           
    def list_books(self):
        """List books"""

        self.clear_screen()
        books=self.catalog_obj.list_books()
        print("check:books:",books)
        if not books:
            tk.Label(self.root,text="No books available.",font=("Arial",12)).pack(pady=10)
        else:
            for book in books:
                tk.Label(self.root,text=str(book)).pack()
        
        tk.Button(self.root,text="Back",command=self.admin_panel,width=15).pack(pady=5)
    def customer_panel(self):
        """Customer Panel"""
        self.clear_screen()
        tk.Label(self.root,text="Customer Panel",font=("Arial",14,"bold")).pack(pady=10)
        tk.Button(self.root,text="View Books",command=self.list_books,width=15).pack(pady=5)
        tk.Button(self.root,text="Logout",command=self.main_screen,width=15).pack(pady=5)
    def clear_screen(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__=="__main__":
    root=tk.Tk()
    app=BookStoreApp(root)
    root.mainloop()

