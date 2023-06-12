#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
function that returns True if the object is exactly an instance of the specified class ;
otherwise False
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to be checked
        a_class (type): The class to be compared to
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
