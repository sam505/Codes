def maxMin(k: int, arr: list) -> int:
    """_summary_

    Args:
        k (int): number of elements to select
        arr (list): an array of integers

    Returns:
        int: minimum possible unfairness
    """
    # Write your code here
    min_unfairness = max(arr)
    
    arr = sorted(arr)
    i = 0
    while i <= len(arr) - k:
        unfairness = max(arr[i:i+k]) - min(arr[i:i+k])
        print(arr[i:i+k])

        if unfairness < min_unfairness:
            min_unfairness = unfairness

        i += 1

    return min_unfairness

    