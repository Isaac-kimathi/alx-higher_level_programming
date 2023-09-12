#!/usr/bin/python
"""Module inherits from the list"""

class MyList(list):
    """A class that inherits from the list"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
