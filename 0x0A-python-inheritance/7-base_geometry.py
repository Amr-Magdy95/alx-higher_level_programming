#!/usr/bin/python3
""" empty base geo class"""


class BaseGeometry:
    """ base geo classs"""
    def area(self):
        """ return the area of the shape"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

