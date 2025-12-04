#!/usr/bin/python3
"""
Module for add_integer function.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.

    a and b must be integers or floats; otherwise a TypeError is raised.
    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
