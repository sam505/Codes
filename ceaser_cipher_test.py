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


def test_three_ceaser_cipher():
    s = "There's-a-starman-waiting-in-the-sky"

    k = 3

    actual = "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb"

    calculated = caesarCipher(s, k)

    assert actual == calculated