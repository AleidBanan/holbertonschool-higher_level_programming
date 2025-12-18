#!/usr/bin/env python3
"""
Module: task_04_flyingfish

This module demonstrates multiple inheritance in Python using
Fish, Bird, and FlyingFish classes, and explores method overriding
and method resolution order (MRO).
"""


class Fish:
    """
    Fish class representing aquatic behavior.
    """

    def swim(self):
        """
        Print swimming behavior of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class representing aerial behavior.
    """

    def fly(self):
        """
        Print flying behavior of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class demonstrating multiple inheritance
    from Fish and Bird.
    """

    def swim(self):
        """
        Override swim behavior.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Override fly behavior.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Override habitat behavior.
        """
        print("The flying fish lives both in water and the sky!")
