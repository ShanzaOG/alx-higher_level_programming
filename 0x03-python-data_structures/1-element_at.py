#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Gets the element in the list
    at a given index
    """
    if idx >= len(my_list) or idx < 0:
        return

    return (my_list[idx])
