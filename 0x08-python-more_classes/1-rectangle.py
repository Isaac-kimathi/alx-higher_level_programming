#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """class represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initialization of a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the private instance attritube"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance attritube"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
