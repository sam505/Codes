from birthdays import *


def test_one_birthdays():
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2

    actual = 2

    calculated = birthday(s, d, m)

    assert actual == calculated


def test_two_birthdays():
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2

    actual = 2

    calculated = birthday(s, d, m)

    assert actual == calculated


def test_three_birthdays():
    s = [1, 1, 1, 1, 1, 1]
    d = 3
    m = 2

    actual = 0

    calculated = birthday(s, d, m)

    assert actual == calculated


def test_four_birthdays():
    s = [4]
    d = 4
    m = 1

    actual = 1

    calculated = birthday(s, d, m)

    assert actual == calculated