import math


def calculate_circle_properties(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius must be non-negative.")

    diameter = float(2 * radius)
    circumference = float(2 * math.pi * radius)
    area = float(math.pi * radius ** 2)

    return (diameter, circumference, area)
