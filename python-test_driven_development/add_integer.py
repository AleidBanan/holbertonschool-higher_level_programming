#!/usr/bin/python3
"""
This module defines a function for adding two numbers with strict type rules.
The function accepts integers or floats, validates them, performs the addition,
and casts the result to an integer. A TypeError is raised for invalid inputs.
"""

def add_integer(a, b=98):
    """
    Add two numbers and return the result as an integer.

    Float inputs are allowed, but the addition is done first and then the
    result is cast to an integer. TypeErrors are raised for invalid inputs.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
