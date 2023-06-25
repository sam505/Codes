def findMedian(arr:list) -> int:
    # Write your code here
    arr = sorted(arr)
    length = len(arr)

    if length % 2 == 0:
        return (arr[int(length/2)] + arr[int(len/2 - 1)])/2
    else:
        return arr[int(length/2)]