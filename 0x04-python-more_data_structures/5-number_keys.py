#!/usr/bin/python3
def number_keys(a_dic):
    num = 0
    list_keys = list(a_dic.keys())

    for i in list_keys:
        num += 1
    return (num)
