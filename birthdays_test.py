from birthdays import *


def test_one_birthdays():
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2

    actual = 2

    calculated = birthday(s, d, m)

    assert actual == calculated