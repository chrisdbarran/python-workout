import chapter3.exercise9 as ex

def test_first_last():
    assert ex.firstlast('abc') == 'ac'
    assert ex.firstlast([1,2,3,4]) == [1,4]
    assert ex.firstlast(('a','b','c','d')) == ('a', 'd')