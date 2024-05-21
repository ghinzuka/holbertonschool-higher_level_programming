#!/usr/bin/python3
"""Write a function that returns True if the object
is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """function that return true or false if object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
