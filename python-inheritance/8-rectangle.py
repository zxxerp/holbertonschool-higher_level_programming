#!/usr/bin/python3
"""Module 8-rectangle: define
s Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheri
    ting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
