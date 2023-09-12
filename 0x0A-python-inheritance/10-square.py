#!/usr/bin/python3
"""Module of a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square"""

    def __innit__(self, size):
        """innitialization of a new square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__innit__(size, size)

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2
