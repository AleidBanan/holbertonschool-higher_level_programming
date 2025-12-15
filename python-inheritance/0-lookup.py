#!/usr/bin/python3
"""
This module provides a function that returns all available
attributes and methods of a given object.
"""


def lookup(obj):
    """
    Returns a list containing the names of all attributes
    and methods available for an object.
    """
    return dir(obj)
