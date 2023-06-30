from page_count import *


def test_one_page_count():
    n = 5
    p = 3

    actual = 1

    calculated = pageCount(n, p)

    assert actual == calculated

    