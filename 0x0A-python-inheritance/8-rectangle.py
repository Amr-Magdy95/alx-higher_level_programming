#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
""" rectangle class module defined """


class Rectangle(BaseGeometry):
    """ rect class definition"""
    def __init__(self, width, height):
        """initialize rect"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
