from sock_merchant import sockMerchant


def test_one_sock_merchant():
    n = 7
    arr = [1, 2, 1, 2, 1, 3, 2]

    actual = 2

    calculated = sockMerchant(n, arr)

    assert actual == calculated


def test_two_sock_merchant():
    n = 7
    arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    actual = 3

    calculated = sockMerchant(n, arr)

    assert actual == calculated     