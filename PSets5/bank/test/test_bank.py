from twttr import shorten

def test_default():
    try:
        assert shorten() == ""
    except TypeError:
        print("No argument")
    
def test_lowercase():
    assert shorten("today") == "tdy"

def test_uppercase():
    assert shorten("BELIVE") == "BLV"

def test_number():
    assert shorten("23") == "23"

def test_punctuatio():
    assert shorten(",.") == ",."
