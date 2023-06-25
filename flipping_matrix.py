def flippingMatrix(matrix: list) -> int:
    # Write your code here
    total = 0
    length = len(matrix)
    n = int(length/2)

    for i in range(n):
        for j in range(n):
            total += max(matrix[i][j], matrix[i][length-j-1], matrix[length-i-1][j], matrix[length-i-1][length-j-1])

    return total
