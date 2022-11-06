# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

from math import pi


class Circle(object):

    def circle_area(self, r):

        area = round(pi * (r ** 2), 2)

        return area


if __name__ == '__main__':
    circle = Circle()
