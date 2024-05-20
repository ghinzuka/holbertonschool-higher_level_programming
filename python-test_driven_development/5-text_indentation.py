#!/usr/bin/python3
"""function that print a text
with newline after threee differents marker ":" "?" "."
avoid to print char if the sentence start with a space
raise: Type error if text is not a string"""


def text_indentation(text):
    """function that print new line after 3 different marker
    raise: if text is not string raise Typerror
    print: new line if marker else print the character
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = ""
    for i in text:
        if i == " " and i == text[0] and char == "":
            char = "\n"
            continue
        if i == " " and char == "\n":
            continue
        if i in [".", "?", ":"]:
            print(i)
            print()
            char = "\n"
        else:
            print(i, end="")
            char = i
