import pytest
import chapter3.exercise9 as ex

@pytest.fixture
def numbers_list():
    return [10,20,30,40,50,60]

@pytest.fixture
def numbers_tuple():
    return (10,20,30,40,50,60)

def test_first_last():
    assert ex.firstlast('abc') == 'ac'
    assert ex.firstlast([1,2,3,4]) == [1,4]
    assert ex.firstlast(('a','b','c','d')) == ('a', 'd')


def test_even_odd_sums(numbers_list, numbers_tuple):
    assert ex.even_odd_sums(numbers_list) == [90,120]
    assert ex.even_odd_sums(numbers_tuple) == [90,120]


def test_plus_minus(numbers_list, numbers_tuple):
    assert ex.plus_minus(numbers_list) == 50
    assert ex.plus_minus(numbers_tuple) == 50

def test_myzip():
    assert ex.myzip([10,20,30], 'abc') == [(10, 'a'), (20, 'b'), (30, 'c')]