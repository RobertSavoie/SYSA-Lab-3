# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

import unittest

from Lab3.app.trapezium import Trapezium


class TestTrapezium(unittest.TestCase):
    def setUp(self):
        self.trapezium = Trapezium()

    def tearDown(self):
        print("\n Result: ", self.shortDescription())

    def test_trapezium_area_radius_less_than_zero(self):
        """Exception raised when radius of trapezium < 0"""
        self.assertEqual(self.trapezium.trapezium_area, -1)
        self.assertRaises(ValueError)

    def test_trapezium_area_greater_than_zero(self):
        """Test area of trapezium when radius >= 0"""
        self.assertEqual(self.trapezium.trapezium_area(10, 5, 6), 45)

    def test_trapezium_area_invalid_input(self):
        """Exception raised when area of trapezium is invalid, boolean, or text"""
        t = self.trapezium.trapezium_area('hello')
        self.assertEqual(t.trapezium_area('hello'))
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
