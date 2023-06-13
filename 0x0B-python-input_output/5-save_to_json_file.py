#!/usr/bin/python3
""" save json to file"""
import json


def save_to_json_file(my_obj, filename):
    """save to json fn"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
