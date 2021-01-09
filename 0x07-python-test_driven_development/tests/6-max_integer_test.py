#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to add Unittests for a function."""

    def test_max_integer(self):
        """Unittest for succes Cases in function
            max_integer.

        Test for:
            list with integers given.
            list with floats given.
            list with negative floats and integer given.
            Empty list.
        """

        self.assertEqual(max_integer([1, 5, 7, 4]), 7)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-5.0, -50, 0]), 0)
        self.assertEqual(max_integer([0.93, 0.92, 0.09]), 0.93)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
