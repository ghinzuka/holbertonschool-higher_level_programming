#!/usr/bin/python3
"""function that returns an object (Python data structure)"""


def from_json_string(my_str):
    """return a string to an object from JSON string"""
    import json
    return json.loads(my_str)
