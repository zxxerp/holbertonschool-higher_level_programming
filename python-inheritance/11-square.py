#!/usr/bin/python3
"""Module 11-square: Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the printable representation of the Square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
