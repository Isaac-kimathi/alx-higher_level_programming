#!/usr/bin/python3

#adds 2 tuples and returns a tuple with 2 integers:
#The first element is the addition of the first element of each argument
#The second element is the addition of the second element of each argument
# If a tuple is smaller than 2, the value 0 is used for each missing integer
# If a tuple is bigger than 2, use only the first 2 integers

def add_tuple(tuple_a=(), tuple_b=()):
    Lg_q = len(tuple_a)
    lg_w = len(tuple_b)
    
    if lg_q < 2:
        if lg_q == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if lg_w < 2:
        if lg_w == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    add_tpl = tuple_a[0] + tupple_b[0], tuple_a[1] + tuple_b[1]
    return add_tpl
