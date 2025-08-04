#!/usr/bin/env python3
"""
This module defines a Book class with methods to represent the book as a string,
provide a detailed representation, and handle deletion of the book instance.
"""


class Book:
    """A class representing a book in a library."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a detailed string representation of the book."""
        return f"Book('{self.title}', '{self.author}', '{self.year}')"

    def __del__(self):
        print(f"Deleting {self.title}")
