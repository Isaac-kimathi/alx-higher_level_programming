#!/usr/bin/python3
"""module for an empty class"""


class BaseGeometry:
    """class representing a base geometry"""

    def area(self):
        """Method not implemented"""
        raise Exception("area() is not implement")

    def integer_validator(self, name, value):
        """validates a value as a integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
