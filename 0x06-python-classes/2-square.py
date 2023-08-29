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
