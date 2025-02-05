class Book:
    """
    A class representing a book in a library system.
    Each book has a title, author, number of pages, and availability status.
    """
    
    def __init__(self, title, author, pages):
        """Initialize a new book object with title, author, pages, and availability."""
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = True

    def checkout(self):
        """Mark the book as checked out if available, otherwise return False."""
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        self.is_available = True
        return True

    def get_info(self):
        """Return a formatted string containing book details and availability status."""
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} ({self.pages} pages) - {availability}"

# Testing Book Class
def test_book_class():
    print("=== Testing Book Class ===")
    
    title = input("Enter the book name: ")
    author = input("Enter the author name: ")
    pages = int(input("Enter the number of pages: "))
    
    book = Book(title, author, pages)
    
    print("\nTest 1: Initial state")
    print("Initial book info:", book.get_info())
    
    print("\nTest 2: First checkout attempt")
    print("Checkout successful?", book.checkout())
    print("After checkout:", book.get_info())
    
    print("\nTest 3: Second checkout attempt")
    print("Second checkout successful?", book.checkout())
    
    print("\nTest 4: Return book")
    print("Return successful?", book.return_book())
    print("After return:", book.get_info())

test_book_class()
