#!/usr/bin/python3
"""module checks if object is an instance or an inherited class"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance or inheritted class otherwise false"""
    return (isinstance(obj, a_class))
