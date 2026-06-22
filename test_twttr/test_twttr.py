from twttr import shorten

def test_vowels():
    assert shorten("cow") == "cw"
    assert shorten("COW") == "CW"

def test_numbers():
    assert shorten("c0w") == "c0w"
    assert shorten("C!W") == "C!W"
