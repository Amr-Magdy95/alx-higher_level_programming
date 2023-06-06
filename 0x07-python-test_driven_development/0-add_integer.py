#!/usr/bin/python3
# 0-add_integer.py
""" an integer addition fn"""


def add_integer(a, b=98):
    """ Return addition of a and b
    Args:
        a (int): first operand
        b (int): second operand
    Raises:
        TypeError: if a or b in non-int or non-float
    Return:
        addition of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
