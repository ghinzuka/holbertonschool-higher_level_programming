#!/usr/bin/python3
"""Write a function that returns True if the object
is an instance of the specified class or
the object is an instance of a class that inherited from,
the specified class """


def is_kind_of_class(obj, a_class):
    """function that return true or false if object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
