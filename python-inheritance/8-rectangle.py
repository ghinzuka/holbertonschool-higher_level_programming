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
