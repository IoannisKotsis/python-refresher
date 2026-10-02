from lesson3 import make_counter
import pytest


def test1():
    c = make_counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3


def test2():
    z1 = make_counter()
    assert z1() == 1
    assert z1() == 2
    assert z1() == 3

    z2 = make_counter()
    assert z2() == 1
