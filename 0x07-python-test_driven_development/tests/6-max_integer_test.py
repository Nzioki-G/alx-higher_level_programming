#!/usr/bin/python3
'''Unittest for max_integer([...])'''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        actual = max_integer(list=[7,2,3,8])
        expected = 8
        self.assertEqual(actual, expected)
