from strings_xor import *


def test_one_strings_xor():
    a = "10101"
    b = "00101"

    actual = "10000"

    calculated = strings_xor(a, b)

    assert actual == calculated