#!/usr/bin/python3
"""module checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns true is an instance of class, otherwise return false"""
    return (type(obj) == a_class)
