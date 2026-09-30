from lesson1 import add_visit
import pytest

def test_add_visit1():
    anna = {"id": 7, "name": "Anna", "visits": ["2026-01-10"]}
    assert add_visit(anna, "2026-08-01") == {'id': 7, 'name': 'Anna', 'visits': ['2026-01-10', '2026-08-01']}
    
def test_add_visit2():
    elena = {"id": 8, "name": "Elena", "visits": ["2026-01-10"]}
    assert elena["visits"] == ["2026-01-10"]
     
def test_add_visit3():
    maria = {"id": 8, "name": "Elena", "visits": ["2026-01-10"]}
    assert add_visit(maria, "2026-09-20")["visits"] is not maria["visits"]
    
    