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

    def update(self, *args, **kwargs):
        """
        Update the attribute of the Square
        instance using no-keyword arguments

        Args (in order):
        1st arg: id attribute
        2nd arg: width attribute
        3rd: height attribute
        4th: x attribute
        5th: y attribute
        If **kwargs exists, it is used to update attributes
        with key-val pairs, where each key represents
        an attribute.

        Arg order is not important.
        """
        if args:
            length = len(args)

            if (length >= 1):
                self.id = args[0]
            if (length >= 2):
                self.size = args[1]
            if (length >= 3):
                self.x = args[2]
            if (length >= 4):
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if (k == "id"):
                    self.id = v
                elif (k == "size"):
                    self.size = v
                elif (k == "x"):
                    self.x = v
                elif (k == "y"):
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation
        of Square."""
        return (
            {
                "id": self.id,
                'size': self.size,
                "x": self.x,
                "y": self.y
            }
        )
