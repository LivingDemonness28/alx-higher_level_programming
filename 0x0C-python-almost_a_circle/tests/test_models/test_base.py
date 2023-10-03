#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiate - line 12
"""
import unittest
import os
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
        base = Base("world")
        self.assertEqual("world", base.id)

    def test_float_id(self):
        base = Base(23.6)
        self.assertEqual(23.6, base.id)

    def test_boolean_id(self):
        base = Base(False)
        self.assertEqual(False, base.id)
    
    def test_list_id(self):
        base = Base([21, 22, 23])
        self.assertEqual([21, 22, 23], base.id)

    def test_set_id(self):
        base = Base({21, 22,23})
        self.assertEqual({21, 22,23}, base.id)

    def test_tuple_id(self):
        base = Base((21, 22,23))
        self.assertEqual((21, 22,23), base.id)

    def test_inf_id(self):
        base = Base(float('inf'))
        self.assertEqual(float('inf'), base.id)

    def test_NaN_id(self):
        base = Base(float('nan'))
        self.assertNotEqual(float('nan'), base.id)

    def test_frozenset_id(self):
        base = Base(frozenset({21, 22,23}))
        self.assertEqual(frozenset({21, 22,23}), base.id)

    def test_range_id(self):
        base = Base(range(24))
        self.assertEqual(range(24), base.id)

    def test_bytes_id(self):
        base = Base(b'customID')
        self.assertEqual(b'customID', base.id)

    def test_bytearray_id(self):
        base = Base(bytearray(b'custom'))
        self.assertEqual(bytearray(b'custom'), base.id)

    def test_two_bases_1(self):
        with self.assertRaises(TypeError):
            Base(22, 26)

    def test_memview_id(self):
        base = Base(memoryview(b'custom'))
        self.assertEqual(memoryview(b'custom'), base.id)

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_tjs_square_type(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([square.to_dictionary()])))

    def test_tjs_square_one_dict(self):
        square = Square(1, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([square.to_dictionary()])) == 39)

    def test_tjs_square_two_dicts(self):
        square1 = Square(1, 2, 3, 4)
        square2 = Square(5, 6, 7, 8)
        list_dicts = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 100)

    def test_tjs_rect_type(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_tjs_rectangle_one_dict(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_tjs_rectangle_two_dicts(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect2 = Rectangle(6, 7, 8, 9, 10)
        list_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 150)

    def test_tjs_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_tjs_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_tjs_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_tjs_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

if __name__ == '__main__':
    unittest.main()
