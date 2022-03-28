import Calculator
def test_add2num():
    a = 10
    b = 20
    result = Calculator.add2num(a,b)
    assert result == a+b
def test_sub2num():
    a = 15
    b = 14
    result  = Calculator.sub2num(a,b)
    assert result == a-b
def test_mul2num():
    a = 54
    b = 71
    result = Calculator.mul2num(a,b)
    assert result == a*b
def test_div2num():
    a = 45
    b = 10
    result = Calculator.div2num(a,b)
    assert result == a/b