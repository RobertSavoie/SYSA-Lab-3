# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

from math import pi


class Rhombus(object):

    def rhombus_area(self, p, q):

        area = round((p * q) / 2)

        return area


if __name__ == '__main__':
    rhombus = Rhombus()
