#!/usr/bin/python3
# div by 2

def divisible_by_2(my_list=[]):
    """find all mults of 2"""
    mults = []
    for i in range(len(my_list)):
        if my_list[i] % 2 ==0:
            mults.append(True)
        else:
            mults.append(False)
    return (mults)
