#!/usr/bin/python3
""" function that add two integer
b is set to 98 by default
if a or b are not float or int raise an error
return the sum of the int of a and b
"""


def add_integer(a, b=98):
    """
    Add two integers or floats, converting them to integers if necessary.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
