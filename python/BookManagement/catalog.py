class Catalog:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance =super().__new__(cls)
            cls._instance.books=[]
        return cls._instance
    def add_book(self,book):
        self.books.append(book)

        print(f"Added book:{book}")

    def remove_book(self,title):
        for book in self.books:
            if book.title==title:
                self.books.remove(book)
                print(f"Removed book:{book}")
                return 
            
        print(f"Book with title {title} not found.")
    def list_books(self):
        if not self.books:
            print("No books in the catalog.")
            return None
        else:
            for book in self.books:
                print(book)
            return self.books
        
    def check_book_present(self,title):
        if(title in book.title for book in self.books):
            return True
        else:
            return False
    def search_books(self,query):
        found_books=[book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.genre.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found.")
                