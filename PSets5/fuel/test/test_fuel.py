from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/9") == 11
    assert convert("0/1") == 0

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')
    with pytest.raises(ValueError):
        convert('3/2')
    
def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'