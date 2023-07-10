def balancedSums(arr: list) -> str:
    # Write your code here
    i = 0
    while i <= len(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return "YES"
        i += 1
        
    return "NO"
