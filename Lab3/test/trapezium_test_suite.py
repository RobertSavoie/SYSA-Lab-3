# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15
import unittest

from Lab3.test.trapezium_test import TestTrapezium


def trapezium_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTrapezium))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
