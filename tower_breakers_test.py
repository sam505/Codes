from tower_breakers import *


def test_one_tower_breakers():
    n = 2
    m = 6

    actual = 2

    calculated = towerBreakers(n, m)

    assert actual == calculated


def test_two_tower_breakers():
    n = 2
    m = 2

    actual = 2

    calculated = towerBreakers(n, m)

    assert calculated == actual


def test_three_tower_breakers():
    n = 1
    m = 4

    actual = 1

    calculated = towerBreakers(n, m)

    assert actual == calculated
