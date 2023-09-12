#!/usr/bin/python
"""The module that defines a MyList class"""

class MyList(list):
    """A class that inherits from the list"""
    def print_sorted(self):
        """print a sorted list/ascending order"""
        print(sorted(self))
