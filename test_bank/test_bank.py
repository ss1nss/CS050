from bank import value

def test_amount():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("h") == 20
    assert value("cow") == 100
    assert value("HOT DOG") == 20
