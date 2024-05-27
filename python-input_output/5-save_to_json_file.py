#!/usr/bin/python3
"""function to return an object to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """function to return an object to a json file"""
    var = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as file:
        hello = file.write(var)
    return hello
