from math import pi
from numbers import Real


def circle_area(radius: Real) -> float:
    if not isinstance(radius, Real):
        raise TypeError("radius must be a real number")
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return pi * radius ** 2
