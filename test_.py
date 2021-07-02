import pytest
import myfactorial

def test_myfactorial():
    assert myfactorial.factorial(3) == 6

def test_suma():
    assert myfactorial.suma(5, 3) == 8
    assert myfactorial.suma(0, -1) == -1
    assert myfactorial.suma(1.5, .5) == 2
