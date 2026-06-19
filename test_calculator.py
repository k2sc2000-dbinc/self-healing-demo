"""calculator 모듈 테스트. 현재 subtract, divide 에서 실패하도록 되어 있음."""

import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    # 버그가 고쳐지면 통과: 5 - 3 = 2
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    # 버그가 고쳐지면 통과: 0으로 나누면 ValueError 를 던져야 함
    with pytest.raises(ValueError):
        divide(10, 0)
