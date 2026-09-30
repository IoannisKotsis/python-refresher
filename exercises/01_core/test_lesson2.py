from lesson2 import register
import pytest

def test_lesson():
    register(5)
    assert register(10) == [10]
    
def test_lessona():
    assert register(2, [4]) == [4, 2]