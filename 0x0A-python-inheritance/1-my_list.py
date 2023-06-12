#!/usr/bin/python3
""" Module my list """


class MyList(list):
    """ class to print sorted list"""
    def print_sorted(self):
        """ sort a list """
        print(sorted(list(self)))
