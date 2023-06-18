from flipping_bits import *


def test_one_flipping_bits():
    n = 9

    actual = 4294967286

    calculated = flippingBits(n)

    assert actual == calculated


def test_two_flipping_bits():
    n = 2147483647

    actual = 2147483648

    calculated = flippingBits(n)

    assert actual == calculated


def test_three_flipping_bits():
    n = 1

    actual = 4294967294

    calculated = flippingBits(n)

    assert actual == calculated


def test_four_flipping_bits():
    n = 0

    actual = 4294967295

    calculated = flippingBits(n)

    assert actual == calculated
