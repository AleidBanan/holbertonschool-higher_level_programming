#!/usr/bin/python3
"""
This module defines a function for adding two numbers with strict type rules.
Both a and b must be integers or floats. If either argument is a float,
it is cast to an integer before the addition is performed. The function
raises a TypeError when inappropriate types are supplied. No modules
are imported.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats.

    Both arguments are type-checked. Floats are cast to integers before
    performing the addition. A TypeError is raised for invalid types.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
