#!/usr/bin/python3
# max int

def max_integer(my_list=[]):
    """ find biggest int"""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
