from plates import is_valid


def test_1():
    assert is_valid("CS50") == True

def test_2():
    assert is_valid("ECTO88") == True

def test_3():
    assert is_valid("NRVOUS") == True

def test_4():
    assert is_valid("CS05") == False

def test_5():
    assert is_valid("CS50P2") == False

def test_6():
    assert is_valid("3.1416") == False

def test_7():
    assert is_valid("H") == False

def test_8():
    assert is_valid("OUTATIME") == False



