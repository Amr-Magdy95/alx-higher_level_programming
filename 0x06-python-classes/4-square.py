#!/usr/bin/python3
""" Def a class Square."""

class Square:
    """repr a square"""

    def __init__(self, size=0):
        """initialization of a new square

        Args:
            size (int): the size of the new square
        """
        self.size = size
    @property
    def size(self):
        """getter for size"""
        return (size.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the current area"""
        return (self.__size * self.__size)
