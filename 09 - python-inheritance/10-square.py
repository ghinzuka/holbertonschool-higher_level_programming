#!/usr/bin/python3
"""create a class named square that inherit from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherit from rectangle in 9rectangle"""

    def __init__(self, size):
        """get size from rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)
