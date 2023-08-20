#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # returns a new dictionary with all values multiplied by 2
    nw_dic = {}
    for key, value in a_dictionary.items():
        nw_dic[key] = value * 2
    return nw_dic
