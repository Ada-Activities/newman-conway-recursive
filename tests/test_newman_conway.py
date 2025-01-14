from app.main import newman_conway
import pytest

def test_newman_conway_5():
    assert newman_conway(5) == [1,1,2,2,3]

def test_newman_conway_1():
    assert newman_conway(1) == [1]

def test_newman_conway_0():
    assert newman_conway(0) == []

def test_newman_conway_3():
    assert newman_conway(3) == [1,1,2]

def test_newman_conway_8():
    assert newman_conway(8) == [1, 1, 2, 2, 3, 4, 4, 4]

def test_newman_conway_20():
    assert newman_conway(20) == [1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 10, 11, 12]