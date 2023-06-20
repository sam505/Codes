from pangrams import *


def test_one_pangrams():
    s = "The quick brown fox jumps over the lazy dog"

    actual = "pangram"

    calculated = pangrams(s)

    assert actual == calculated


def test_two_pangrams():
    s = "We promptly judged antique ivory buckles for the next prize"

    actual = "pangram"
    
    calculated = pangrams(s)

    assert actual == calculated


def test_three_pangrams():
    s = "We promptly judged antique ivory buckles for the prize"

    actual = "not pangram"
    
    calculated = pangrams(s)

    assert actual == calculated