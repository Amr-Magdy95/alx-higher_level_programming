#!/usr/bin/python3
""" append to file module"""


def append_write(filename="", text=""):
    """ append to file fn"""
    with open(filename, 'a', encode="utf-8") as f:
        return (f.write(text))
