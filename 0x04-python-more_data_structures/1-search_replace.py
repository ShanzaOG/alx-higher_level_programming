#!/us/bin/python3
def search_replace(my_list, search, replace):
    """
    Function to search and replace an element
    """
    new_list = []

    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
