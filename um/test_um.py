import pytest
from um import count

def test_count():
    assert count("Um, aluminum") == 1
    assert count(" um ") == 1
    assert count("um? um? numb") == 2
