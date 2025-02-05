class Book:
    def __init__(self, title, author, pages):  # TODO 1
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = True

    def checkout(self):  # TODO 2
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):  # TODO 3
        self.is_available = True
        return True

    def get_info(self):  # TODO 4
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} ({self.pages} pages) - {availability}"

# Testing function
def test_book_class():
    book = Book("The Hobbit", "J.R.R. Tolkien", 295)
    print(book.get_info())  # Expected: "The Hobbit by J.R.R. Tolkien (295 pages) - Available"
    assert book.checkout() is True
    print(book.get_info())  # Expected: "The Hobbit by J.R.R. Tolkien (295 pages) - Not Available"
    assert book.checkout() is False  # Already checked out
    assert book.return_book() is True
    print(book.get_info())  # Expected: "The Hobbit by J.R.R. Tolkien (295 pages) - Available"

test_book_class()
