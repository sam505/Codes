from .reverse_alpha import *


def test_one_sort_alpha():
    s = "ab-cd"

    actual = "dc-ba"

    calculated = reverse_aplha(s)


def test_two_sort_alpha():
    s = "a-bC-dEf=ghIj!!"

    actual = "j-Ih-gfE=dCba!!"

    calculated = reverse_aplha(s)