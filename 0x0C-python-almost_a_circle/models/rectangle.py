#!/usr/bin/python3
"""Defines rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new Rectangle

        Args:
            width (int): Width coordinate of the new Rectangle.
            height (int): Height coordinate of the new Rectangle.
            x (int): x coordinate of the new Rectangle.
            y (int): y coordinate of the new Rectangle.
            id (int): identity of the new Rectangle.
        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height is smaller than 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y are smaller than or equal to 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get width coordinate of Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if (value <= 0):
            raise ValueError("width must be > 0")
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """set/get height coordinate of Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if (value <= 0):
            raise ValueError("height must be > 0")
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """set/get x coordinate of Rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        if (value < 0):
            raise ValueError("x must be >= 0")
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """set/get y coordinate of Rectangle."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if (value < 0):
            raise ValueError("y must be >= 0")
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        self.__y = value
