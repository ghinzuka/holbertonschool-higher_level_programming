#!/usr/bin/python3
"""class with a method that raise and excpetion
and raise error if value is not good"""


class BaseGeometry:
    """class with a method to raise area"""
    def area(self):
        """ raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that raise errors and return the value as name"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
