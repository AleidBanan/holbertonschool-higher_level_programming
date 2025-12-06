#!/usr/bin/python3
"""
Module 4-print_square
Contain one method that the size must be integer and greater than zero
Print square with the character #
"""


def print_square(size):
    """Print square with character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    # For size 0, print nothing at all (no newline)
    if size == 0:
        return

    # For size >= 1, print the square and end with a newline (as required)
    message = "\n".join(["#" * size for _ in range(size)])
    print(message)
