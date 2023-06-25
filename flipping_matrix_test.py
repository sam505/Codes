from flipping_matrix import *


def test_one_flipping_matrix():
    matrix = [[1, 2], [3, 4]]

    actual = 4

    calculated = flippingMatrix(matrix)

    assert actual == calculated


def test_two_flipping_matrix():
    matrix = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108]
    ]

    actual = 414

    calculated = flippingMatrix(matrix)

    assert actual == calculated