#!/usr/bin/python3
"""Defines square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of square.
            x (int): x-coordinate of square's position (default is 0).
            y (int): y-coordinate of square's position (default is 0).
            id (int): ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size of square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """set size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a formatted string representation
        of a Square.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
