"""
This module provides classes for managing books and a library.
It includes functionality to add books, check them out, and return them.
"""


class Book:
    def __init__(self, title, author, is_checked_out=False):
        """Initialize a book with a title, author, and checked-out status."""
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out

    def is_checked_out(self):
        """Check if the book is currently checked out."""
        return self.__is_checked_out

    def return_book(self):
        """Return the book, marking it as not checked out."""
        self.__is_checked_out = False

    def set_checked_out(self, checked_out):
        """Set the checked-out status of the book."""
        self.__is_checked_out = checked_out


class Library:
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self.__books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.__books.append(book)

    def check_out_book(self, title):
        """
        Check out a book from the library by title.
        If the book is available, mark it as checked out.
        """
        for book in self.__books:
            if book.title == title and not book.is_checked_out():
                book.set_checked_out(True)
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Return a book to the library by title.
        If the book is checked out, mark it as returned.
        """
        for book in self.__books:
            if book.title == title and book.is_checked_out():
                book.set_checked_out(False)
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' is not available for return.")

    def list_available_books(self):
        """
        List all books that are currently available (not checked out).
        """
        available_books = [book for book in self.__books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
