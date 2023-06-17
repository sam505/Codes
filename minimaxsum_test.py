from minimaxsum import *


def test_miniMaxSum_one():
    arr = [1, 3, 5, 7, 9]

    actual = [16, 24]

    calculated = miniMaxSum(arr)

    assert actual == calculated


def test_miniMaxSum_two():
    arr = [1, 2, 3, 4, 5]

    actual = [10, 14]

    calculated = miniMaxSum(arr)

    assert actual == calculated