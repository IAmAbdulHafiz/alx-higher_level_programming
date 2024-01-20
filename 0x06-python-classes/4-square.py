#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get/set the current size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)
