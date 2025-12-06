#!/usr/bin/python3
"""
Module 0-add_integer
Contains one function that adds two integers or floats.
Floats are casted to integers before addition.
"""


def add_integer(a, b=98):
    """
    Add two numbers after validating their types.

    Args:
        a (int/float): first number
        b (int/float): second number (default=98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers/floats
        OverflowError: if a or b are infinite
        ValueError: if a or b are NaN
    """
    # Validate types (no bools allowed)
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    # Handle NaN and infinity cases explicitly
    if isinstance(a, float):
        if a != a:
            raise ValueError("cannot convert float NaN to integer")
        if a in [float('inf'), float('-inf')]:
            raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float):
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        if b in [float('inf'), float('-inf')]:
            raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
