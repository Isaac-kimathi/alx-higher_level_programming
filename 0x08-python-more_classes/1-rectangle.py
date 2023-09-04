#!/usr/bin/pythhon3
"""A class that defines a rectangle"""


class Rectangle:
    """class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializing the rectangle class
        PARAS:
            weight: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size isn't integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attritube"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attritube"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attritube"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
