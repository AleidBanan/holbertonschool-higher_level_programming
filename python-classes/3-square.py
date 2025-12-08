#!/usr/bin/python3
"""Module that defines a Square class with area calculation capability."""


class Square:
    """Square class that can calculate its area based on size."""

    def __init__(self, size=0):
        """Initialize a new Square instance with optional validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
