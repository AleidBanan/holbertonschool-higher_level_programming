#!/usr/bin/python3
"""
This module provides a function that checks whether an object
is an instance of a specified class or a class derived from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified
    class or an instance of a class that inherits from it,
    otherwise returns False.
    """
    return isinstance(obj, a_class)
