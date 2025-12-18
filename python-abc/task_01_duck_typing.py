#!/usr/bin/env python3
"""
Module: task_01_duck_typing
Demonstrates abstract base classes and duck typing.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle defined by radius."""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def shape_info(obj: Shape) -> None:
    """
    Print area and perimeter of a shape using duck typing.
    
    Relies on the object having area() and perimeter() methods.
    """
    print(f"Area: {obj.area():.2f}")
    print(f"Perimeter: {obj.perimeter():.2f}")


# Optional: Test when running this module directly
if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
