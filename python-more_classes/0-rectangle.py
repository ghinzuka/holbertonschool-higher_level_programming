#!/usr/bin/python3
"""create a function that returns a rectangle"""


class Rectangle:
    """class rectangle with private widht and private lenght"""

    def __init__(self, width=0, height=0):
        """initiate widht and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the private value of with"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """get the value value of width if is int and positiv number"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve the private value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """get the value value of width if is int and positiv number"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
