from find_zigzag_sequence import findZigZagSequence


def test_one_find_zigzag_sequence():
    seq = [2, 3, 5, 1, 4]

    actual = [1, 4, 5, 3, 2]

    calculated = findZigZagSequence(seq, len(seq))

    assert actual == calculated


