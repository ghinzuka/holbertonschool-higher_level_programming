#!/usr/bin/env python3
"""class shape with abstract method area and perimeter"""


from abc import ABC, abstractmethod


class Shape(ABC):
    """abstract class from ABC"""
    @abstractmethod
    def area(self):
        """abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method perimeter"""
        pass


class Circle(Shape):
    """class circle from shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """area of circle using pi to the suare of radius"""
        return (3.141592653589793 * (self.radius ** 2))

    def perimeter(self):
        """caclulating perimeter using pi and radius"""
        return (2 * 3.141592653589793 * self.radius)


class Rectangle(Shape):
    """class rectangle from shape with two methods are and perimeter"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """return area using widht and height from init"""
        return (self.width * self.height)

    def perimeter(self):
        """return perimeter adding widht and height by two"""
        return (2 * (self.width + self.height))


def shape_info(shape):
    """shape method for duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
