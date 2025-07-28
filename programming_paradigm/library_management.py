"""
This module provides classes for managing books and a library.
It includes functionality to add books, check them out, and return them.
"""


class Book:
    def __init__(self, title, author):
        """Initialize a book with a title, author, and checked-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Return True if the book is currently checked out, else False."""
        return self._is_checked_out

    def set_checked_out(self, status):
        """Set the checked-out status of the book."""
        self._is_checked_out = status


class Library:
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book from the library by title.
        If the book is available, mark it as checked out.
        """
        for book in self._books:
            if book.title == title and not book.checked_out():
                book.set_checked_out(True)
                # print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Return a book to the library by title.
        If the book is checked out, mark it as returned.
        """
        for book in self._books:
            if book.title == title and book.checked_out():
                book.set_checked_out(False)
                # print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' is not available for return.")

    def list_available_books(self):
        """
        List all books that are currently available (not checked out).
        """
        available_books = [book for book in self._books if not book.checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
