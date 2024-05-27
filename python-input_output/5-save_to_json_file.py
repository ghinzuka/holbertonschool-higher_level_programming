#!/usr/bin/python3
"""function to return an object to a json file"""


def save_to_json_file(my_obj, filename):
    """function to return an object to a json file"""
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj, ensure_ascii=False))
