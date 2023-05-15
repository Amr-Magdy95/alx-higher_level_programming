#!/usr/bin/python3
# print list integer

def print_list_integer(my_list=[]):
    """Print all ints in a list"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
