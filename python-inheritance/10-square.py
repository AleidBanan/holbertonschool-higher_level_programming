#!/usr/bin/python3
"""Module: Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the square with size as private attribute"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
