#!/usr/bin/python3
""" mod for class or subclass"""


def is_kind_of_class(obj, a_class):
    """ is class or subclass"""
    return (type(obj) is a_class or issubclass(obj, a_class))
