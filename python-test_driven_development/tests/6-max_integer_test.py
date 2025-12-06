#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer"""

    def test_all_negative(self):
        """Test all negatives with max at beginning, middle, and end"""
        self.assertEqual(max_integer([-45, -67, -12]), -12)
        self.assertEqual(max_integer([-81, -22, -92]), -22)
        self.assertEqual(max_integer([-100, -97, -35]), -35)

    def test_max_integer(self):
        """Test for any integer number"""
        self.assertEqual(max_integer([10, 0, -2]), 10)
        self.assertEqual(max_integer([-3, -7, 0, -2]), 0)

    def test_empty_list(self):
        """Test for empty list []"""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Test for no argument"""
        self.assertIsNone(max_integer())

    def test_one_argument(self):
        """Test one argument"""
        self.assertEqual(max_integer([-1]), -1)

    def test_none_argument(self):
        """Test for None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_wrong_type(self):
        """Test for wrong data type"""
        string = [1, 3, "wrong"]
        with self.assertRaises(TypeError):
            max_integer(string)


if __name__ == "__main__":
    unittest.main()
