#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """class represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialization of a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """converts the class rectangle instance to a str"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for column in range(self.__height):
                for row in range(self.__width):
                    try:
                        rectangle_str += str(self.print_symbol)
                    except exception:
                        rectangle_str += type(self).print_symbol
                if column < self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str.rstrip()

    def __repr__(self):
        """returns a str reprsentation of the rectangle object"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
