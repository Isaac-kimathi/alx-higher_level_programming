#!/usr/bin/python3
"""The module defines a class called student"""


class Student:
    """class definning a student"""

    def __init__(self, first_name, last_name, age):
        """iniatializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved
        Otherwise, all attributes must be retrieved

        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__
