#!/usr/bin/python3
"""defines a rectangle with height and width"""


class Rectangle:
    """init method comes first
        Args:
        height - the height of the rectangle
        width - the width of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    @property
    def width(self):
        """Set the new width"""
        return(self.__width)

    @width.setter
    def width(self,value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the new height"""
        return(self.__height)

    @height.setter
    def width(self,value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
