#!/usr/bin/python3
"""functin that print a file.txt"""


def read_file(filename=""):
    """open and print a file .txt"""
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")
