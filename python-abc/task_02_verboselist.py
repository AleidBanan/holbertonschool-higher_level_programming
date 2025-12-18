#!/usr/bin/env python3
"""
Module: task_02_verboselist

This module defines the VerboseList class, which extends Python's
built-in list class. VerboseList provides additional console
notifications whenever items are added to or removed from the list.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when modified.

    Overrides append, extend, remove, and pop methods to provide
    verbose output while preserving original list behavior.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at the given position and print a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
