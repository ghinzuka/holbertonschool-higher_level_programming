#!/usr/bin/python3
"""create a function that returns a rectangle"""


class Rectangle:
    """class rectangle with private widht and private lenght
return: area
return: perimeter
print via __str__ a string representation of a rectangle
print message when delted with __del__
return: via __repr__ a representation of the rectangle used by eval
return: via bigger_or_equal the bigger area size between two instance

"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initiate new instance for each call of method in main"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __del__(self):
        """print a message when deleting an instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    @property
    def width(self):
        """retrieve the private value of with"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """get the value value of width if is int and positiv number"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve the private value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """get the value value of width if is int and positiv number"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return the permimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns string representation of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rows = [
            str(self.print_symbol) * self.__width
            for i in range(self.__height)
            ]
        return "\n".join(rows)

    def __repr__(self):
        """return a representation of Ractangle to be used by eval"""
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        or typeError if not an instance of rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return (cls(size, size))
