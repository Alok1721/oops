class Review:
    def __init__(self,book,user,rating,comment):
        self.book=book
        self.user=user
        self.rating=rating
        self.comment=comment

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}: {self.rating}/5 - {self.comment}"
    