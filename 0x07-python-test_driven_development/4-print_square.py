#!/usr/bin/python3
# 4-print_square.py
""" Defines a fn that prints square"""


def print_square(size):
    """ print a square with the # char

    Args:
        size (int): side of square
    Raises:
        TypeError: if size in not int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
