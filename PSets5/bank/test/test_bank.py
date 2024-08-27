from bank import value

def test_default():
    assert value("hello") == 0
    
def test_hello_name():
    assert value("hello, david") == 0

def test_how():
    assert value("How you doing?") == 20

def test_what():
    assert value("What's happening?") == 100
