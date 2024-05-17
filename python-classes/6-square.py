#!/usr/bin/python3
"""Create a class with a private instance with private size attribute in """


class Square:
    """Initializes a private method to give size and raise errors
    and creat a public instance for area
    """
    def __init__(self, size=0, position=(0, 0)):
        """give the size to the __size attribute
        and position 0 to __position
        """
        self.__size = size
        self.__position = position
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

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
        """
        

    def area(self):
        """
        return the calculated area of the
        square using the predefine self.__size initialize
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ print in stdout the square with the # char"""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
