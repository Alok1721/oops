class Book:
    def __init__(self,title,author,genre,price):
        self.title=title
        self.author=author
        self.genre=genre
        self.price=price

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})-${self.price}"