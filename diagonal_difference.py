def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0

    for i in range(len(arr)):
        diag1 += arr[i][i]
        diag2 += arr[i][-1-i]

    return abs(diag1 - diag2)
