#!/usr/bin/python3
""" is subclass mod"""


def inherits_from(obj, a_class):
    """ is subclass of """
    return (False if type(obj) is a_class else isinstance(obj, a_class))
