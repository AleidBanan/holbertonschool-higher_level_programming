#!/usr/bin/env python3
"""
Module: task_05_dragon

This module demonstrates the use of mixin classes to add
independent behaviors (swimming and flying) to a Dragon class.
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines swimming and flying abilities
    using mixins.
    """

    def roar(self):
        """
        Print roaring behavior.
        """
        print("The dragon roars!")
