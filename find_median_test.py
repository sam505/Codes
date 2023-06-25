from find_median import *


def test_one_find_median():
    arr = [5, 3, 1, 2, 4]

    actual = 3

    calculated = findMedian(arr)

    assert actual == calculated


def test_two_find_median():
    arr = [0, 1, 2, 4, 6, 5, 3]

    actual = 3

    calculated = findMedian(arr)

    assert actual == calculated