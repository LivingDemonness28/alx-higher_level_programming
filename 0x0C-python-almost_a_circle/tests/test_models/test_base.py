#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiate - line 12
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiate(unittest.TestCase):
    """Unittests for instantiation of the Base class."""
    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

if __name__ == '__main__':
    unittest.main()
