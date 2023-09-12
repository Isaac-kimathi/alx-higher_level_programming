#!/usr/bin/python3
"""module if an instance is inherited dirctly/indirectly from a class"""


def inherits_from(obj, a_class):
    """returns True is an instance is inherited, otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
