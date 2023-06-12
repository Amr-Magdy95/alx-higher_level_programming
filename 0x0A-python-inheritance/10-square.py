#!/usr/bin/python3
""" class square module"""
Rectangle = __import__("9-Rectangle").Rectangle


class Square(Rectangle):
    """ Square class definition"""
    def __init__(self, size):
        """initialize class square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ return area of square"""
        return (self.__size * self.__size)
