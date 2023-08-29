#!/usr/bin/python3

"""A module that defining a square """


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square instance.

        args: size - The size of the square. Default is 0.
        type: size - int
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current area of the square.

        return: The area of the square.
        rtype: int
        """
        return self.__size ** 2
