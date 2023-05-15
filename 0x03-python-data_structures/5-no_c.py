#!/usr/bin/python3
# no c

def no_c(my_string):
    """ remove all C's from string"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
