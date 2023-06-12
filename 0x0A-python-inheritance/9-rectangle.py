#!/usr/bin/python3
""" rect class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rect class definition"""
    def __init__(self, width, height):
        """initialize rect"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """ returns the area of the rectangle"""
        return (self.width *self.height)
    def __str__(self):
        """ str repr of the obj"""
        return "[Rectangle] {}/{}".format(self.width, self.height)
