#!/usr/bin/python3
"""function that returns the dictionary description"""


import pickle


class CustomObject:
    """CustomObject class"""

    def __init__(self, name, age, is_student):
        """initialize the object attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display the object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is_student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize the object"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError, FileNotFoundError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserialize the object"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (pickle.UnpicklingError, FileNotFoundError):
            return None
