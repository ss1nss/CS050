from plates import is_valid

def test_order():
    assert is_valid("BA") == True
    assert is_valid("1B") == False
    assert is_valid("13") == False
    assert is_valid("0B") == False
    assert is_valid("1") == False

def test_len():
    assert is_valid("BE") == True
    assert is_valid("BEA321") == True
    assert is_valid("BEA3211") == False


def test_alphanum():
    assert is_valid("BE2345") == True
    assert is_valid("BEA321") == True
    assert is_valid("BEA021") == False
    assert is_valid("BEA12B") == False
    assert is_valid("111111") == False


def test_specialchar():
    assert is_valid("CW0!") == False
    assert is_valid(".CO0") == False
    assert is_valid("CW30!") == False
