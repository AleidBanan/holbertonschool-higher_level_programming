#!/usr/bin/python3
"""
This module provides a function add_integer(a, b=98)
that adds two integers or floats after casting to int.
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
