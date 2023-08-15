#!/usr/bin/python3

#removes all characters c and C from a string and return the new string
def no_c(my_string):
    nw_str = my_string.translate({ord('C'): None})
    nw_str = nw_str.translate({ord('c'): None})
    return nw_str
