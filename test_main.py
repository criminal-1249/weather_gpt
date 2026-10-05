import pytest
from main import add, divide


def test_add_basic():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add_large_numbers():
    assert add(10**18, 10**18) == 2 * 10**18


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_divide_basic():
    assert divide(10, 2) == 5
    assert divide(-4, 2) == -2


def test_divide_float():
    assert divide(1, 3) == pytest.approx(0.3333333333333333)


def test_divide_zero_numerator():
    assert divide(0, 5) == 0


def test_divide_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_divide_large_numbers():
    assert divide(10**18, 10**9) == 10**9


