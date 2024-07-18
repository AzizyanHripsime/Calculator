import pytest
from contextlib import nullcontext as does_not_raise
from src.main import Calculator

class TestCalculator:

    @pytest.mark.parametrize('x, y, res, expectation', [
        (3, 2, 1.5, does_not_raise()),
        (4, 2, 2, does_not_raise()),
        (5, 0, 5, pytest.raises(ZeroDivisionError)),
        ('5', 2, 2.5, pytest.raises(TypeError))
        ])
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x,y)==res

    @pytest.mark.parametrize('x,y,res, expectation', [
        (2, 2, 4, does_not_raise()),
        (3, 2, 5, does_not_raise()),
        ('5', 2, 7, pytest.raises(TypeError))
    ])
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res

    @pytest.mark.parametrize('x,y,res, expectation', [
        (5, 2, 3, does_not_raise()),
        (0, -3, 3, does_not_raise()),
        ('5', 2, 7, pytest.raises(TypeError))
    ])
    def test_minus(self, x, y, res, expectation):
        with expectation:
            assert Calculator().minus(x, y) == res

    @pytest.mark.parametrize('x,y,res, expectation', [
        (5, 2, 10, does_not_raise()),
        (2, 2, 4, does_not_raise()),
        ('5', 2, 10, pytest.raises(TypeError))
    ])
    def test_mul(self, x, y, res, expectation):
        with expectation:
            assert Calculator().mul(x, y) == res