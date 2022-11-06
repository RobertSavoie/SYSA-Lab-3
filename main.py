# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

from Lab3.test.circle_test_suite import circle_suite
from Lab3.test.ellipse_test_suite import ellipse_suite
from Lab3.test.rhombus_test_suite import rhombus_suite
from Lab3.test.trapezium_test_suite import trapezium_suite

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
        circle_suite()
        cont = False
    elif selection == "t":
        trapezium_suite()
        cont = False
    elif selection == "e":
        ellipse_suite()
        cont = False
    elif selection == "r":
        rhombus_suite()
        cont = False
    elif selection == "q":
        cont = False
    else:
        print("Please enter a valid input.")
        cont = False
