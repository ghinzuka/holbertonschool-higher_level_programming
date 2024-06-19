#!/usr/bin/python3
"""function that print a square
size : argument must be an int and above or equal to 0
raise : TypeError if no int
Raise: ValluError if under 0
Print: # square shape lenght of size
"""


def print_square(size):
    """function that print a suare shape with # character"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size, end="")
        print()
