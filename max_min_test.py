from max_min import maxMin


def test_one_max_min():
    arr = [1, 4, 7, 2]

    k = 2

    actual = 1
    calculated = maxMin(k, arr)
    
    assert actual == calculated


def test_two_max_min():
    arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

    k = 4

    actual = 3
    calculated = maxMin(k, arr)
    
    assert actual == calculated


def test_three_max_min():
    arr = [1, 2, 1, 2, 1]

    k = 2

    actual = 0
    calculated = maxMin(k, arr)
    
    assert actual == calculated

    
def test_four_max_min():
    with open("max_min.txt", "r") as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    k = 2430

    actual = 2374
    calculated = maxMin(k, arr)
    
    assert actual == calculated