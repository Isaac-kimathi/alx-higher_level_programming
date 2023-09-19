#!/usr/bin/python3
"""This module contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """retrieves the value for height"""
        return self.__height

    @property
    def x(self):
        """retrieves the value for x"""
        return self.__x

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if(type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """sets the value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")

        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return (self.__height * self.__width)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """redefines of the format for the string represenation of a class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            ac = 0
            for av in args:
                if ac == 0:
                    if av is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = av
                elif ac == 1:
                    self.width = av
                elif ac == 2:
                    self.height = av
                elif ac == 3:
                    self.x = av
                elif ac == 4:
                    self.y = av
                ac += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rec_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return rec_dictionary
