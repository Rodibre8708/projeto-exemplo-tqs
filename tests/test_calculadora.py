import pytest
from src.calculadora import soma, subtrai, divide

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
