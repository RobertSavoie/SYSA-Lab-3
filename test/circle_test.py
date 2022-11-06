# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.

    def tearDown(self):
        print("\n end of test ", self.shortDescription())

    def test_circle_area_radius_less_than_zero(self):
        """Exception raised when radius of circle < 0"""
        c=Circle(-1)
        self.assertEqual(c.radius,-1)
        self.assertRaises(ValueError)

    def test_circle_area_greater_than_zero(self):
        """Test area of circle when radius >= 0"""
        c=Circle(10)
        self.assertEqual(c.radius,10)

    def test_circle_area_invalid_input(self):
        """Exception raised when area of circle is invalid, boolean, or text"""
        c=Circle('hello')
        self.assertEqual(c.radius,'hello')
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
