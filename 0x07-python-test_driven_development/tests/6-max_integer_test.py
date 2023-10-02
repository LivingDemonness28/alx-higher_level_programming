#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests max_integer([..])."""

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Chocolate", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [22, 23, 25, 24]
        self.assertEqual(max_integer(unordered), 25)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [22, 23, 24, 25]
        self.assertEqual(max_integer(ordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [25, 24, 23, 22]
        self.assertEqual(max_integer(max_at_beginning), 25)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [24]
        self.assertEqual(max_integer(one_element), 24)

    def test_floats(self):
        """Test a list of floats."""
        floats = [10.6, -7.25, 9.56, 9.2, 6.0]
        self.assertEqual(max_integer(floats), 10.6)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [56.36, 1.5, -89, 5, 6]
        self.assertEqual(max_integer(ints_and_floats), 56.36)

    def test_string(self):
        """Test a string."""
        string = "Chocolate"
        self.assertEqual(max_integer(string), 't')

if __name__ == '__main__':
    unittest.main()
