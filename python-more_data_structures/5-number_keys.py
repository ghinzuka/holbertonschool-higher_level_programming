#!/usr/bin/python3
def number_keys(a_dictionary):
    res = 0
    for key in a_dictionary:
        res += 1
        if isinstance(a_dictionary[key], dict):
            res += number_keys(a_dictionary[key])
    return res
