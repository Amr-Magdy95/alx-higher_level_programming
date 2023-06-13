#!/usr/bin/python3
"""load obj module"""
import json


def load_from_json_file(filename):
    """load from json obj fn"""
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
