from page_count import *


def test_one_page_count():
    n = 5
    p = 3

    actual = 1

    calculated = pageCount(n, p)

    assert actual == calculated


def test_two_page_count():
    n = 6
    p = 2

    actual = 1

    calculated = pageCount(n, p)

    assert actual == calculated


def test_three_page_count():
    n = 6
    p = 3

    actual = 1

    calculated = pageCount(n, p)

    assert actual == calculated


def test_four_page_count():
    n = 21235
    p = 17

    actual = 8

    calculated = pageCount(n, p)

    assert actual == calculated