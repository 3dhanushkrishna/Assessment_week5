import pytest
import Question1

@pytest.mark.xfail
@pytest.mark.parametrize("x,res",[(25,5),(36,6),(12,3)])
def test_square_root(x,res):
    sqrt=Question1.square_root(x)
    assert sqrt == res

@pytest.mark.skip(reason="no need")
@pytest.mark.parametrize("a,b,c,res",[(2,3,4,5)])
def test_quadratic_equation(a,b,c,res):
    quatreq=Question1.quadratic_equation(a,b,c)
    assert quatreq == res

@pytest.mark.parametrize("celsius,res",[(3,37.4),(4,32.0)])
def test_cels_to_farh(celsius,res):
    cel=Question1.cels_to_farh(celsius)
    assert cel == res

@pytest.fixture
def input():
    x=12
    return x
def test_pos_neg_zero(input):
    res=Question1.pos_neg_zero(input)
    assert res == "positive"

@pytest.mark.parametrize("num,res",[(16,136),(10,100)])
def test_natural_num(num,res):
    natnum=Question1.natural_num(num)
    assert natnum == res