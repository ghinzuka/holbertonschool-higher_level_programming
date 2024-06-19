#!/usr/bin/python3
"""
check if the object as a dict to add a name attribute and it's value to it
other wise return an error that the attributes can't be added
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
