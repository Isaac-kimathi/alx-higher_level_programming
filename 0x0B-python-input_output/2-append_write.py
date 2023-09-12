#!/usr/bin/python3
"""The module defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of text file and returns chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
