#!/usr/bin/python3
def uppercase(s):
    uppercase_string = ""
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            uppercase_string += uppercase_char
        else:
            uppercase_string += char
    print(uppercase_string)
