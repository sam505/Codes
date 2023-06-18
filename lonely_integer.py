def lonelyinteger(a: list) -> int:
    """Function that gets the lonely integer in a list

    Args:
        a (list): a list containing integers

    Returns:
        int: an interger that only appears once in the list
    """
    for num in a:
        if a.count(num) == 1:
            return num