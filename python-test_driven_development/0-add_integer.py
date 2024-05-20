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
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return (a + b)
