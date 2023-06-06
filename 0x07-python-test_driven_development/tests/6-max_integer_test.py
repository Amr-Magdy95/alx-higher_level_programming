#!/usr/bin/python3
# 6-max_integer_test.py
""" unit test for max integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ define a unittest for max integer"""
    def test_ordered_list(self):
        """ test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)
    def test_unordered_list(self):
        """ test unordered list"""
        l = [3, 1, 4, 2]
        self.assertEqual(max_integer(l), 4)
    def test_max_at_beginning(self):
        """ max at idx 0"""
        l = [4, 3, 2, 1]
        self.assertEqual(max_integer(l), 4)
    def test_empty_list(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)
    def test_one_element(self):
        """ one elem list"""
        self.assertEqual(max_integer([7]), 7)
    def test_floats(self):
        """ testing floats"""
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 2.4]), 3.4)
    def test_mixed(self):
        """ tests ints and floats"""
        self.assertEqual(max_integer([1, 5, 6, 5.5, 6.6, 4.5]), 6.6)

if __name__ == "__main__":
    unittest.main()
