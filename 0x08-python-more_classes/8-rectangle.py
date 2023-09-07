#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        print_symbol (int): Symbol used for str representation.
        number_of_instances (int): Num of Rectangle instances.
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """get the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """get the printable representation of Rectangle

        Represents rectangle with with # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_list = []
        for i in range(self.__height):
            [rect_list.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                rect_list.append("\n")
        return ("".join(rect_list))

    def __repr__(self):
        """get the string representation of Rectangle"""
        rect_list = "Rectangle(" + str(self.__width)
        rect_list += ", " + str(self.__height) + ")"
        return (rect_list)

    def __del__(self):
        """print message for deletion of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """get the Rectangle with greater area
        
        Args:
            rect_1 (Rectangle): 1st Rectangle.
            rect_2 (Rectangle): 2nd Rectangle.
        
        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        return (rect_2)
