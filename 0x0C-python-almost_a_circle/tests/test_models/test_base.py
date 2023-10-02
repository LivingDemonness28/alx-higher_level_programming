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
    def test_two_bases(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

if __name__ == '__main__':
    unittest.main()
