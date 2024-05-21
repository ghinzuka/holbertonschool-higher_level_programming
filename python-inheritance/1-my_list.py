#!/usr/bin/python3
"""class to inherit from list"""


class MyList(list):
    """class Mylist that inherit from list
    method print sorted : print in ascending order the list inherated"""

    def print_sorted(self):
        res = sorted(self)
        print(res)
