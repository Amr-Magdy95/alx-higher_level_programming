#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
""" rectangle class """


class Rectangle(BaseGeometry):
    """ rect class"""
    def __init__(self, width, height):
        """initialize rect"""
        self.validate_integer("width", width)
        self.validate_integer("height", height)
        self.__width = width
        self.__height = height
