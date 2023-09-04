#!/usr/bin/pythhon3
"""A class that defines a rectangle"""


class Rectangle:
    """class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            weight: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieval of width attritube"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting of width attribute"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieval of height attritube"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting of height attritube"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
