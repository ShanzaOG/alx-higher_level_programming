#!/usr/bib/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds two tuples together and
    returns a tuple
    """
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    new_tuple = ()

    for i in range(2):
        if i >= len1:
            a = 0
        else:
            a = tuple_a[i]
        if i >= len2:
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            new_tuple = (a + b)
        else:
            new_tuple = (new_tuple, a + b)
    return (new_tuple)
