import Calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(5,1,6),(8,2,10),(5,2,9)])
def test_add2num(a,b,c):

    result = Calculator.add2num(a,b)
    assert result == c
@pytest.mark.addsub
def test_sub2num():
    a = 15
    b = 14
    result  = Calculator.sub2num(a,b)
    assert result == a-b

@pytest.mark.muldiv
def test_mul2num():
    a = 54
    b = 71
    result = Calculator.mul2num(a,b)
    assert result == a*b

@pytest.mark.muldiv
def test_div2num():
    a = 45
    b = 10
    result = Calculator.div2num(a,b)
    assert result == a/b
