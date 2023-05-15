#!/usr/bin/python3
# 2-replace in list

def replace_in_list(my_list, idx, element):
    """replace an element of a list"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
