#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            new_dict = {}
            for i in self.__dict__:
                for j in attrs:
                    if i == j:
                        new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__
