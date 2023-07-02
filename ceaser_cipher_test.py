from Ceaser_cipher import *


def test_one_ceaser_cipher():
    s = "middle-Outz"

    k = 2

    actual = "okffng-Qwvb"

    calculated = caesarCipher(s, k)

    assert actual == calculated


def test_two_ceaser_cipher():
    s = "Always-Look-on-the-Bright-Side-of-Life"

    k = 5

    actual = "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

    calculated = caesarCipher(s, k)

    assert actual == calculated