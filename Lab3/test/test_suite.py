# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15
import unittest

from Lab3.test.circle_test import TestCircle
from Lab3.test.rhombus_test import TestRhombus
from Lab3.test.ellipse_test import TestEllipse
from Lab3.test.trapezium_test import TestTrapezium


def my_suite():
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    cont = True
    while cont:
        print("\nPlease select from one of the following options:\n"
              "- [c] for testing the area of a circle\n"
              "- [t] for testing the area of a trapezium\n"
              "- [e] for testing the area of an ellipse\n"
              "- [r] for testing the area of a rhombus\n"
              "- [q] to quit\n")
        selection = input("What would you like to do? ")

        if selection == "c":
            suite.addTest(unittest.makeSuite(TestCircle))
            print(runner.run(suite))
            cont = False
        elif selection == "t":
            suite.addTest(unittest.makeSuite(TestTrapezium))
            print(runner.run(suite))
            cont = False
        elif selection == "e":
            suite.addTest(unittest.makeSuite(TestEllipse))
            print(runner.run(suite))
            cont = False
        elif selection == "r":
            suite.addTest(unittest.makeSuite(TestRhombus))
            print(runner.run(suite))
            cont = False
        elif selection == "q":
            cont = False
        else:
            print("Please enter a valid input.")
            cont = False


my_suite()
