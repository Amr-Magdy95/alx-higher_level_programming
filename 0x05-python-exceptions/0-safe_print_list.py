#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """PRINT x elements of a list
    Args:
        my_list (list): the list
        x (int): num of elems
    Returns: 
        num of elem printed
    """
    ret = 0
    for i in range(x);
        try:
            print("{}".format(my_list[i], end=""))
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
