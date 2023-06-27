def sockMerchant(n:int, ar:list) -> int:
    """_summary_

    Args:
        n (int): number of socks
        ar (list): socks available

    Returns:
        int: number of pairs available
    """
    # Write your code here
    socks = set(ar)

    pairs = 0

    for sock in socks:
        pairs += int(ar.count(sock)/2)

    return pairs