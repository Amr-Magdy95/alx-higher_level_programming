#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    list_ord = list(a_dic.keys())
    list_ord.sort()
    for i in list_ord:
        print("{}: {}".format(i, a_dic.get(i)))
