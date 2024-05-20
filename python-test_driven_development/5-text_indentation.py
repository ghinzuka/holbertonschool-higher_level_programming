#!/usr/bin/python3
"""function"""


def text_indentation(text):
    """function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == " " and i is text[0]:
            i =""
        if i == "." or i == "?" or i == ":":
            print(i)
            print()
        else:
            print(i, end="")
