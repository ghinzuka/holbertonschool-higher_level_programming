#!/usr/bin/python3
"""function that returns JSON representation of an objec"""


def to_json_string(my_obj):
    """function that returns JSON representation of an object"""
    import json
    return json.dumps(my_obj)
