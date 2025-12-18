#!/usr/bin/python3
'''7-base_geometry.py
Module that contain an empty class'''


class BaseGeometry():
    '''Creating an empty class with an empty method'''

    def area(self):
        '''Raising an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Raising exception if the integer is not valid'''
        if value is None:
            raise TypeError(f"{name} must be an integer")
        elif type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return True
