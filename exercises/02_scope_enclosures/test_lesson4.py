from lesson4 import make_alert
import pytest


def test_upper():
    fever = make_alert(38)
    assert fever(39) == True


def test_lower():
    fever = make_alert(38)
    assert fever(37) == False


def test_equal():
    fever = make_alert(38)
    assert fever(38) == False


def test_2different():
    fever = make_alert(38)
    bpm = make_alert(100)
    assert fever(40) == True
    assert bpm(99) == False
