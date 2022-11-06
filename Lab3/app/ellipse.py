# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

from math import pi


class Ellipse(object):
    def ellipse_area(self, a, b):
        area = round(pi * a * b)

        return area


if __name__ == '__main__':
    ellipse = Ellipse()
