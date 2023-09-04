#!/usr/bin/pythhon3
"""A class defining a rectangle"""


class Rectangle:
    """Class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Writes the width and height elements"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width element"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width element"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of height element"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height element"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
