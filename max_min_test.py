from max_min import maxMin


def test_one_max_min():
    arr = [1, 4, 7, 2]

    k = 2

    actual = 1
    calculated = maxMin(2, arr)
    
    assert actual == calculated


def test_two_max_min():
    arr = [4, 1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

    k = 2

    actual = 3
    calculated = maxMin(2, arr)
    
    assert actual == calculated
