# Megan Gagliardi & Rob Savoie
# SYSA 3204
# 11/5/2022
# Lab 3 - Group 15

class Trapezium(object):
    def trapezium_area(self, a, b, h):
        area = round(((a + b) / 2) * h)

        return area


if __name__ == '__main__':
    trapezium = Trapezium()
