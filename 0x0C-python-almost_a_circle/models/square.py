#!/usr/bin/python3
"""Defines square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
        - size (int): Size of square.
        - x (int): x-coordinate of square's position (default is 0).
        - y (int): y-coordinate of square's position (default is 0).
        - id (int): ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a formatted string representation
        of a Square.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
