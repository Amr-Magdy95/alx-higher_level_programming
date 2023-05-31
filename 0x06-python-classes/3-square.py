#!/usr/bin/python3
""" Def a class Square."""

class Square:
    """repr a square"""

    def __init__(self, size=0):
        """initialization of a new square

        Args:
            size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Return the current area"""
        return (self.__size * self.__size)
