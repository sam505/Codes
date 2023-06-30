from find_zigzag_sequence import findZigZagSequence


def test_one_find_zigzag_sequence():
    seq = [2, 3, 5, 1, 4]

    actual = [1, 2, 5, 4, 3]

    calculated = findZigZagSequence(seq, len(seq))

    assert actual == calculated


def test_two_find_zigzag_sequence():
    seq = [1, 2, 3, 4, 5, 6, 7]

    actual = [1, 2, 3, 7, 6, 5, 4]

    calculated = findZigZagSequence(seq, len(seq))

    assert actual == calculated