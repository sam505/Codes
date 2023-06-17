def miniMaxSum(arr):
    min_sum = sum(arr) - max(arr)

    max_sum = sum(arr) - min(arr)
    print(min_sum, max_sum)
    return [min_sum, max_sum]


