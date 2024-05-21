#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 5]), 5)
        self.assertEqual(max_integer([-2, -4, -5, -6]), -2)
        self.assertEqual(max_integer([2]), 2)

