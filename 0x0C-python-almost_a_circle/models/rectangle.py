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
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get height coordinate of Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get x coordinate of Rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get y coordinate of Rectangle."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints Rectangle using '#' char."""
        for j in range(self.y):
            print()

        for i in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """Returms formatted string representation of
        Rectangle instance."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - " +
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        Update the attribute of the Rectangle
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
                self.width = args[1]
            if (length >= 3):
                self.height = args[2]
            if (length >= 4):
                self.x = args[3]
            if (length >= 5):
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                if (k == "id"):
                    self.id = v
                elif (k == "width"):
                    self.width = v
                elif (k == "height"):
                    self.height = v
                elif (k == "x"):
                    self.x = v
                elif (k == "y"):
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation
        of Rectangle."""
        return (
            {
                "id": self.id,
                'width': self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        )
