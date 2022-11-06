# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15
import unittest

from Lab3.app.rhombus import Rhombus


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.rhombus = Rhombus()

    def tearDown(self):
        print("\n Result: ", self.shortDescription())

    def test_circle_area_radius_less_than_zero(self):
        """Exception raised when radius of rhombus < 0"""
        self.assertEqual(self.rhombus.rhombus_area(-1, -1), -1)
        self.assertRaises(ValueError)

    def test_circle_area_greater_than_zero(self):
        """Test area of rhombus when dimensions >= 0"""
        self.assertEqual(self.rhombus.rhombus_area(10, 10), 50)

    def test_circle_area_invalid_input(self):
        """Exception raised when area of rhombus is invalid, boolean, or text"""
        c = self.rhombus.rhombus_area('hello')
        self.assertEqual(c.radius, 'hello')
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
