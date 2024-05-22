#!/usr/bin/python3
"""class with a method that raise and excpetion
and raise error if value is not good"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherated from base geometry"""

    def __init__(self, width, height):
        """give height and width if integer validator is true"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area base on height and width from init"""
        return (self.__width * self.__height)

    def __str__(self):
        """return a printable string with area"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
