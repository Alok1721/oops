class Order:
    def __init__(self,cart):
        self.cart=cart
    def place_order(self):
        print(f"Order placed successfully")
        print("Items in order")
        for book in self.cart.items:
            print(book)