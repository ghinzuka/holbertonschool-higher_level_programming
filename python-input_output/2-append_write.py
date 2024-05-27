#!/usr/bin/python3
"""defines function to read n lines of a text file"""


def append_write(filename="", text=""):
    """appends string to text file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
