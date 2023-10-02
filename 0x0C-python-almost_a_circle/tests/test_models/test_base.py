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
    
    def test_id_public_atr(self):
        base = Base(24)
        base.id = 9
        self.assertEqual(9, base.id)

    def test_dictionary_id(self):
        self.assertEqual({"a": 56, "b": 102}, Base({"a": 56, "b": 102}).id)

    def test_complex_id(self):
        self.assertEqual(complex(26), Base(complex(26)).id)

    def test_string_id(self):
        self.assertEqual("world", Base("world").id)

    def test_float_id(self):
        self.assertEqual(23.6, Base(23.6).id)

    def test_boolean_id(self):
        self.assertEqual(False, Base(False).id)
    
    def test_list_id(self):
        self.assertEqual([21, 22,23], Base([21, 22,23]).id)

    def test_set_id(self):
        self.assertEqual({21, 22,23}, Base({21, 22,23}).id)

    def test_tuple_id(self):
        self.assertEqual((21, 22,23), Base((21, 22,23)).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

if __name__ == '__main__':
    unittest.main()
