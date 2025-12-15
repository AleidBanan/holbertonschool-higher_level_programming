#!/usr/bin/python3
"""Module: BaseGeometry class"""

class BaseGeometry:
    """BaseGeometry class with an unimplemented area method"""

    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")
