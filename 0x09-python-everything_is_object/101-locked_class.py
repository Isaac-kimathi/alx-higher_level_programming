#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevents instatiation of attributes except attribute called first_name
    """

    __slots__ = ["first_name"]
