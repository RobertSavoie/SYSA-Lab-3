# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15
import unittest

from Lab3.test.ellipse_test import TestEllipse


def ellipse_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEllipse))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
