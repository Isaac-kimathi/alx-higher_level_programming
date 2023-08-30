#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        intg = 0
        grp = 0
        for tup in my_list:
            intg += (tup[0] * tup[1])
            grp += (tup[1])
        return (intg/grp)
    return 0
