import pytest
from main import add, divide


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(2.5, 3.5) == 6.0


def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5


def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5


def test_divide_large_numbers():
    assert divide(10**12, 10**6) == 10**6
