#!/usr/bin/python3
"""module defining class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class inheritting from the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization of square attributes"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer""")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates arguments assigned to attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and value is not None:
                        raise TypeError("Id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                            raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """that returns the dictionary representation of a Square"""
        squ_dictionary = {"id": self.id, "size": self.size,
                          "x": self.x, "y": self.y}

        return squ_dictionary
