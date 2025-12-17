#!/usr/bin/python3
"""Module 7-base_geometry: define add public instance method"""


class BaseGeometry:
    """class basegeometry use public instance method"""

    def area(self):
        """raise an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
