import pytest
from fuel import convert
from fuel import gauge

def test_fraction():
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("1/1") == 100

def test_percent():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"

def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("3/1")
