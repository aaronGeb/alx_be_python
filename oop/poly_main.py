#!/usr/bin/env python3

from polymorphism_demo import Circle, Rectangle


def main():
    shapes = [Rectangle(10, 5), Circle(7)]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()
