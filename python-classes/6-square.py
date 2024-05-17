#!/usr/bin/python3
"""Create a class with a private instance with private size attribute
and a position to print a square shape of # or space at position"""


class Square:
    """Initializes a private method to give size and raise errors
    and creat a public instance for area
    """
    def __init__(self, size=0, position=(0, 0)):
        """give the size to the size attribute
        and position 0 to position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve the size"""
        """ Returns: the lenght of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):

        """ set the value of the size"""
        """ args: Val: the lenght of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the value of the position in private
        args : value : the position
        raise : type error if val is not int or value is not tuple
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        return the calculated area of the
        square using the predefine self.__size initialize
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ print in stdout the square with the # char
        or nothing in the position
        """
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
