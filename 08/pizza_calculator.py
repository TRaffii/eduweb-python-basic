from math import pi, pow


def calculate_pizza_cm(price, dimension):
    radius = dimension / 2
    return price / (pi * pow(radius, 2))

