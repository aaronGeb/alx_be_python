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

    def is_checked_out(self):
        """Return True if the book is currently checked out, else False."""
        return self._is_checked_out

    def check_out(self):
        """Return True if the book is currently checked out"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return True if the book is currently checked out"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True

        return False

    def __str__(self):
        status = "Available" if self._is_checked_out else "Checked Out"
        return f"{self.title} by {self.author} - {status}"


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
            if book.title.lower() == title.lower() and not book.is_checked_out():
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return a book to the library by title.
        If the book is checked out, mark it as returned.
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_checked_out():
                # print(f"Returned: {book.title}")
                return
        return False

    def list_available_books(self):
        """
        List all books that are currently available (not checked out).
        """
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
