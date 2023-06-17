from time_conversion import *


def test_one_timeConversion():
    s = "12:01:00PM"

    actual = "12:01:00"

    calculated = timeConversion(s)

    assert actual == calculated


def test_two_timeConversion():
    s = "7:05:45PM"

    actual = "19:05:45"

    calculated = timeConversion(s)

    assert actual == calculated

def test_three_timeConversion():
    s = "12:40:22AM"

    actual = "00:40:22"

    calculated = timeConversion(s)

    assert actual == calculated