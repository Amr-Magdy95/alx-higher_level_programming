#!/usr/bin/python3
""" empty base geo class"""


class BaseGeometry:
    """ base geo classs"""
    def area(self):
        """ return the area of the shape"""
        raise Exception("area() is not implemented")
