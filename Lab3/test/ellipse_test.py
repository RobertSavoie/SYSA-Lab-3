# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

import unittest

from Lab3.app.ellipse import Ellipse


class TestEllipse(unittest.TestCase):
    def setUp(self):
        self.ellipse = Ellipse()

    def tearDown(self):
        print("\n end of test ", self.shortDescription())

    def test_ellipse_area_radius_less_than_zero(self):
        """Exception raised when dimensions of ellipse < 0"""
        self.assertEqual(self.ellipse.ellipse_area(-1, -1), -1)
        self.assertRaises(ValueError)

    def test_ellipse_area_greater_than_zero(self):
        """Test area of ellipse when dimensions >= 0"""
        self.assertEqual(self.ellipse.ellipse_area(5, 7), 109.96)

    def test_ellipse_area_invalid_input(self):
        """Exception raised when area of ellipse is invalid, boolean, or text"""
        e = self.ellipse.ellipse_area('hello')
        self.assertEqual(e.radius, 'hello')
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
