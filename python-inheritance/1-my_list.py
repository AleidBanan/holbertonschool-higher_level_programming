#!/usr/bin/python3
"""
This module defines a custom list class that can display
its elements in sorted order without modifying the list.
"""


class MyList(list):
    """
    MyList extends the built-in list class by adding
    a method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order
        without changing the original list.
        """
        print(sorted(self))
