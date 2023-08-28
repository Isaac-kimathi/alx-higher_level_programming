#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element by element.
    Args:
    my_list_1 (list): The first list.
    my_list_2 (list): The second list.
    list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new = []
    try:
        for n in range(list_length):
            try:
                res = my_list_1[n] / my_list_2[n]
            except ZeroDivisionError:
                print("division by 0")
                res = 0
            except (TypeError, ValueError):
                print("wrong type")
                res = 0
            except IndexError:
                print("out of range")
                res = 0
            finally:
                new.append(res)
    finally:
        return new_list
