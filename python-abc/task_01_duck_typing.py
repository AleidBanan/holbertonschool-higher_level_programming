#!/usr/bin/env python3
"""
Module: task_01_duck_typing
Demonstrates abstract base classes and duck typing.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    """Circle defined by radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print shape area and perimeter using duck typing."""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
