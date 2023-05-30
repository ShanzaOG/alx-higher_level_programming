#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:18:54 2023
@author: ShanzaOG
"""

class Square:
    """Class Square with attributes. Instantiation with size
    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The init method for class Square
        Args:
            size: A private instance size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
