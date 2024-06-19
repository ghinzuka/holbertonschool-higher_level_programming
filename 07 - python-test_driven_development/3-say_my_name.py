#!/usr/bin/python3
"""function that print first and last name
first name and last name has to be a string
Raise: Type error if not first name not str
raise: Type error if last name not str
print with .format to print two variables
"""


def say_my_name(first_name, last_name=""):
    """ function that print two variables containing string in it
    by default last name is empty
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
