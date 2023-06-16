from plusminus import *


def test_plusMinus_one():
    arr = [-4, 3, -9, 0, 4, 1]
    actual = (0.500000, 0.333333, 0.166667)

    result = plusMinus(arr)

    assert actual == result


def test_plusMinus_two():
    arr = [1, 1, 0, -1, -1]
    actual = (0.400000, 0.400000, 0.200000)

    result = plusMinus(arr)

    assert actual == result