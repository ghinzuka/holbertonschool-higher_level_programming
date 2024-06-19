#!/usr/bin/python3
"""Create a class with a private instance with private size attribute in """


class Square:
    """Initializes a private method to give size and raise errors
    and creat a public instance for area
    """
    def __init__(self, size=0):
        """give the size to the __size attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        return the calculated area of the
        square using the predefine self.__size initialize
        """
        return (self.__size * self.__size)
