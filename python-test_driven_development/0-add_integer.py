#!/usr/bin/python3
"""
This module provides a function that adds two integers.

Both a and b may be integers or floats. If either argument is a float,
it is cast to an integer before the addition is performed. A TypeError
is raised if the inputs are not numbers. No modules are imported.
"""

def add_integer(a, b=98):
    """
    Add two numbers after casting floats to integers.

    Args:
        a: first number (int or float)
        b: second number (int or float, default 98)

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
