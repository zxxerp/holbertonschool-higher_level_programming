#!/usr/bin/python3
"""Module 6-base_geometry:
    defines BaseGeometry with unimplemented area method"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an
        Exception indicating the area method is not implemented"""
        raise Exception("area() is not implemented")
