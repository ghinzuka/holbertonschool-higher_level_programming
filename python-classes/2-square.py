#!/usr/bin/python3
"""Create a class with a private instance with private size attribute in """


class Square:
    """Initializes a private size and raise errors """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
