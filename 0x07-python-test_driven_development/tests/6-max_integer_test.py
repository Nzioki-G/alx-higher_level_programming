#!/usr/bin/python3
'''Unittest for max_integer([...])'''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer(list=[7,2,3,8]), 8)
        self.assertEqual(max_integer(list=[]), None)
        self.assertEqual(max_integer(list=[1,1,1]), 1)
        self.assertEqual(max_integer(list=[7]), 7)
        self.assertRaises(max_integer(list=8), TypeError)
        self.assertRaises(max_integer(list=[7,2,'3']), ValueError)
