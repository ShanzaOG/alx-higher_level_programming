#!/us/bin/python3
def search_replace(my_list, search, replace):
    """
    Function to search and replace an element
    """
    return ([elem if elem != search else replace for elem in my_list])
