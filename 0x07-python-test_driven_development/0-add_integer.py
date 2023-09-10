#!/usr/bin/python3
"""
Module containing only a function that adds 2 integers
"""

def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b

    Args:
        a: first argument
        b: second argument

    Returns:
        sum of the two arguments

    Raises:
        TypeError: if either of the arguments not an integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
