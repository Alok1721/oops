class Cart:
    def __init__(self):
        self.items=[]
    def add_item(self,book):
        self.items.append(book)
        print(f"Added to cart:{book}")

    def remove_item(self,title):
        for book in self.items:
            if book.title==title:
                self.items.remove(book)
                print(f"Removed from cart:{book}")
                return 
        print(f"Book with title {title} not found in cart")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty")
        else:
            for book in self.items:
                print(book)