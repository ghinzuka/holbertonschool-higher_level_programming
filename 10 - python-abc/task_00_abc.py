#!/usr/bin/python 3
"""define an abstract method in an abstract class inherit from ABC"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """create an class inherit from ABC"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """subclass inherit from Animal"""
    def sound(self):
        """method to return a string"""
        return "Bark"


class Cat(Animal):
    """subclass inherit from Animal"""
    def sound(self):
        """method to return string"""
        return "Meow"
