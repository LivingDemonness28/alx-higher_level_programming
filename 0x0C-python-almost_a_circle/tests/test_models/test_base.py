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
    def test_None_two_bases(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_unique_id(self):
        base = Base(24)
        self.assertEqual(24, base.id)
    
    def test_unique_id_sequence(self):
        base1 = Base()
        base2 = Base(42)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_two_bases(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base2.id, base3.id - 2)

if __name__ == '__main__':
    unittest.main()
