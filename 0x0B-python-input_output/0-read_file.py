#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
