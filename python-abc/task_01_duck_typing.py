#!/usr/bin/python3
"""
Module: task_01_duck_typing

This module demonstrates the concept of duck typing using an abstract
base class Shape and concrete implementations Circle and Rectangle.
It also provides a function that operates on any object implementing
the required interface (area and perimeter methods).
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Any class that inherits from Shape must implement
    the area() and perimeter() methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class representing a circular shape.

    Inherits from Shape and implements the required methods.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a radius.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * self.radius ** 2
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Rectangle class representing a rectangular shape.

    Inherits from Shape and implements the required methods.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Print the area and perimeter of a shape.

    This function demonstrates duck typing by calling
    area() and perimeter() without checking the object's type.

    Args:
        obj: Any object that implements area() and perimeter().
    """
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
