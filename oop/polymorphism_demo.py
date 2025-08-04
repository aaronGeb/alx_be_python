import math

"""This module demonstrates polymorphism with shapes."""


class Shape:
    def area(self):
        """Method to calculate area, to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
