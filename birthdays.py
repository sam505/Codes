def birthday(s:list, d:int, m:int) -> int:
    """_summary_

    Args:
        s (list): a list
        d (int): an integer, sum of segment
        m (int): an integer, length of segment

    Returns:
        int: an integer
    """
    # Write your code here
    pieces = 0

    while len(s) >= m:
        if sum(s[:m]) == d:
            s.pop(0)
            pieces += 1
        else:
            s.pop(0)
    
    return pieces



        
            
