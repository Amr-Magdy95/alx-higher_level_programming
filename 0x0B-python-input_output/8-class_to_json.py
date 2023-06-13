#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """class to json fn"""
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return (dic)
