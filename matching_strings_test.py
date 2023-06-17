from matching_strings import *

def test_one_matching_strings():
    strings = ["ab", "ab", "abc"]
    queries = ["ab", "abc", "bc"]

    actual = [2, 1, 0]

    expected = matchingStrings(strings, queries)

    assert actual == expected


def test_two_matching_strings():
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]

    actual = [2, 1, 0]

    expected = matchingStrings(strings, queries)

    assert actual == expected


def test_three_matching_strings():
    strings = ["def", "de", "fgh"]
    queries = ["de", "lmn", "fgh"]

    actual = [1, 0, 1]

    expected = matchingStrings(strings, queries)

    assert actual == expected


def test_four_matching_strings():
    strings = ["abcde", "sdaklfj", "asdjf","na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"]
    queries = ["abcde", "sdaklfj", "asdjf", "na", "basdn"]

    actual = [1, 3, 4, 3, 2]

    expected = matchingStrings(strings, queries)

    assert actual == expected