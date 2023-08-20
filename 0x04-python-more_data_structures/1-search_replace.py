#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_lst = []
    for element in my_list:
        if element == search:
            nw_lst.append(replace)
        else:
            nw_lst.append(element)

    return nw_lst
