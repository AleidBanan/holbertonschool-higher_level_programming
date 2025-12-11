#!/usr/bin/python3
"Defines a Rectangle class."


class Rectangle:
    "Represents a rectangle."

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        "Retrieve width."
        return self.__width

    @width.setter
    def width(self, value):
        "Set width with vali
