from balanced_sum import *

def test_one_balanced_sum():
    arr = [5, 6, 8, 11]

    actual = "YES"

    calculated = balancedSums(arr)

    assert actual == calculated


def test_two_balaned_sum():
    arr = [1, 2, 3]

    actual = "NO"

    calculated = balancedSums(arr)

    assert actual == calculated


def test_three_balanced_sum():
    arr = [1, 2, 3, 3]

    actual = "YES"

    calculated = balancedSums(arr)

    assert actual == calculated