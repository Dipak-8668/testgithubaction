from src.math_operations import add , sub

def test_add():
    assert add(2,3)==5
    assert add(10,2)==12
    assert add(-1,1) == 0

def test_sub():
    assert sub(10,2)==8
    assert sub(5,2)==3
    assert sub(5,8) ==-3 