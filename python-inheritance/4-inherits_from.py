#!/usr/bin/python3
"""Write a function that returns True only if
the object is an instance of a class that inherited from,
the specified class """


def inherits_from(obj, a_class):
    """function that return true if object is an instance inherited"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
