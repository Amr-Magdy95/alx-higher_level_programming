#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write file function"""
    with open(filename, 'r', encoding="utf-8") as f:
        return len(list(f))
