from lesson3 import make_counter
import pytest


def test_counter_increments_by_one():
    c = make_counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3


def test_counters_are_independent():
    z1 = make_counter()
    assert z1() == 1
    assert z1() == 2
    assert z1() == 3

    z2 = make_counter()
    assert z2() == 1
