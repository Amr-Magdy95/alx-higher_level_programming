#!/usr/bin/python3
""" class student module"""


class Student:
    """class student definition"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ class dic"""
        return (self.__dict__.copy())
