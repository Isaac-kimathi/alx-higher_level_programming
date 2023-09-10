#!/usr/bin/python3
"""
The module contains a function that indents texts
"""

def text_indentation(text):
    """
    Function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text(str): The string to be printed

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cnt = 0
    while cnt < len(text) and text[cnt] == " ":
        cnt = cnt + 1

    while cnt < len(text):
        print(text[cnt], end="")
        if text[cnt] == "\n" or text[cnt] in ".?:":
            if text[cnt] in ".?:":
                print("\n")
            cnt = cnt + 1
            while cnt < len(text) and text[cnt] == " ":
                cnt = cnt + 1
            continue
        cnt = cnt + 1
