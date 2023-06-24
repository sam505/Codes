from two_arrays import *


def test_one_two_arrays():
    a = [0, 1]
    b = [0, 2]
    k = 1 

    actual = "YES"

    calculated = twoArrays(k, a, b)

    assert actual == calculated


def test_two_two_arrays():
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10

    actual = "YES"

    calculated = twoArrays(k, a, b)

    assert actual == calculated


def test_three_two_arrays():
    a = [1, 2, 2, 1]
    b = [3, 3, 3, 4]
    k = 5

    actual = "NO"

    calculated = twoArrays(k, a, b)

    assert actual == calculated