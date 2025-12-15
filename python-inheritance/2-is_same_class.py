#!/usr/bin/python3
"""
This module provides a function that checks whether an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the
    specified class, otherwise returns False.
    """
    return type(obj) is a_class
