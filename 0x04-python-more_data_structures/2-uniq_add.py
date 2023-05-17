#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Function to add unique elements in a list
    """

    uniq_set = set(my_list)
    uniq_sum = sum(uniq_set)
    return uniq_sum
