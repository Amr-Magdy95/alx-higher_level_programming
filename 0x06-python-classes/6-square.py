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
        self.position = position
    @property
    def size(self):
        """getter for size"""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """get the curr position"""
        return (self.__position)
    @position.setter
    def position(self, value):
        if (not instance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """Return the current area"""
        return (self.__size * self.__size)
    def my_print(self):
        """ print the square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
