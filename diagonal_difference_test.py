from diagonal_difference import *


def test_one_diagonal_difference():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]

    actual = 2

    calculated = diagonalDifference(arr)

    assert actual == calculated


def test_two_diagonal_difference():
    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]

    actual = 15

    calculated = diagonalDifference(arr)

    assert actual == calculated