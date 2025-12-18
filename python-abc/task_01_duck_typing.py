#!/usr/bin/env python3
"""
Module: task_01_duck_typing

This module demonstrates the use of abstract base classes (ABC)
and duck typing to handle different shapes uniformly.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class that defines the interface for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape defined by its radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape defined by width and height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    This function relies on duck typing and does not check
    the object's type explicitly.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
