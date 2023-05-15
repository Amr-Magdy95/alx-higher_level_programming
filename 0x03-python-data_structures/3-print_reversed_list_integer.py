#!/usr/bin/python3
# print rev list

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in rev"""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
