import pytest
from seasons import change

def test_change():
    assert change(2) == "Two thousand, eight hundred eighty minutes"
    assert change(0) == "Zero minutes"
    assert change(365) == "Five hundred twenty-five thousand, six hundred minutes"
