#!/usr/bin/env python3
"""
Module: task_03_countediterator

This module defines the CountedIterator class, which wraps a standard
Python iterator and keeps track of how many items have been iterated.
"""


class CountedIterator:
    """
    Iterator that counts how many items have been fetched.

    This class wraps an existing iterable and increments an internal
    counter each time an item is retrieved using __next__().
    """

    def __init__(self, iterable):
        """
        Initialize the counted iterator.

        Args:
            iterable: Any iterable object (list, tuple, etc.).
        """
        self.iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Raises:
            StopIteration: When no more items are available.
        """
        item = next(self.iterator)   # May raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over.

        Returns:
            int: Number of fetched items.
        """
        return self._count
