#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # returns a new dictionary with all values multiplied by 2
    nw_dr = a_dictionary.copy()
    keys_n_list = list(nw_dr.keys())

    for x in keys_n_list:
        nw_dr[x] *= 2

    return (nw_dr)
