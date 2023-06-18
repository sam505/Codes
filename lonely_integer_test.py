from lonely_integer import *

def test_one_lonelyinteger(a):
    a = [1, 2, 3, 4, 3, 2, 1]

    actual = 4

    calculated = lonelyinteger(a)

    assert actual == calculated


