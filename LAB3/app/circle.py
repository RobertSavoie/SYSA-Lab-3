# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

from math import pi


class Circle(object):

    def circle_area(r):
        return pi * (r ** 2)

    # radii = [2, 0, -3, 2 + 5j, True, "radius"]
    # message = "Area of circles with r = {radius} is {area}"
    #
    # for r in radii:
    #     A = circle_area(r)
    #     print(message.format(radius=r, area=A))


if __name__ == '__main__':
    circle = Circle()
