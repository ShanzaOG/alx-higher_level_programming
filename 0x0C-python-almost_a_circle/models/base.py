#!/usr/bin/python3

"""
class Base
"""

class Base:
    """
    class Base

    Attributes:
        nb_objects (int): Private class attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor

        Attributes:
            id (int): integer input
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
