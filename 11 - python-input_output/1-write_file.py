#!/usr/bin/python3
"""function that write file.txt"""


def write_file(filename="", text=""):
    """function that create and write in a file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        read = f.read()
    return len(read)
