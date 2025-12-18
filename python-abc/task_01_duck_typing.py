#!/usr/bin/env python3
"""
Module: task_01_duck_typing

This module demonstrates the concept of duck typing in Python using
an abstract base class Shape and concrete implementations Circle and
Rectangle. It also includes a function that operates on any object
that provides the required methods, without checking its type.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    Any subclass must implement the area() and perimeter() methods.
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
    Circle class that represents a circle shape.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
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


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    This function relies on duck typing: it assumes the passed object
    implements area() and perimeter(), without checking its type.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
