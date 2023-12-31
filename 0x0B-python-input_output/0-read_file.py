#!/usr/bin/python3
"""module defines a function that reads a text file and prints it out"""


def read_file(filename=""):
    """Reads and prints the contents of a UTF8 text file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
