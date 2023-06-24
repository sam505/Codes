def twoArrays(k:int, A:list, B:list) -> str:
    """_summary_

    Args:
        k (int): an integer
        A (list): a list
        B (list): a list

    Returns:
        str: a string (YES or NO)
    """
    
    a_sorted = sorted(A, reverse=False)
    b_sorted = sorted(B, reverse=True)

    for i in range(len(A)):
        if a_sorted[i] + b_sorted[i] < k:
            return "NO"
    
    return "YES"