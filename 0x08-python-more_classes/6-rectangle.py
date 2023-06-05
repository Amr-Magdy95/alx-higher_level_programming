#!/usr/bin/python3
# 1-rectangle.py
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes a rect
        Args:
            width (int): the width of the rect
            height (int): the height of the rect
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get/Set the width of the rect"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the rect"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rect"""
        return((self.__width) * (self.__height))

    def perimeter(self):
        """ returns the perimeter of the rect"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ returns the printable representation of the rect"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return the string repr of the rect"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ print deletion msg"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
