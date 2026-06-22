from numb3rs import validate

def test_octet():
    assert validate("125") == False
    assert validate("cat") == False
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.256") == False
    assert validate("255.255.255.255.") == False
