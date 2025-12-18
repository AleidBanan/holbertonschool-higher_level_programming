#!/usr/bin/env python3
"""
Module: task_00_abc

This module defines an abstract base class Animal using the ABC package.
It also defines two subclasses, Dog and Cat, that implement the abstract
method sound().
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class defines a blueprint for animals and enforces the
    implementation of the sound() method in subclasses.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    Implements the sound() method.
    """

    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    Implements the sound() method.
    """

    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: "Meow"
        """
        return "Meow"
