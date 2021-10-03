import chapter3.exercise10 as ex

def test_mysum():
    assert ex.mysum(1,2,3) == 6
    assert ex.mysum('abc', 'def') == 'abcdef'
    assert ex.mysum([1,2,3],[4,5,6]) == [1,2,3,4,5,6]


def test_mysum_bigger_than():
    assert ex.mysum_bigger_than(10, 5, 20, 30, 6) == 50
    assert ex.mysum_bigger_than('def', 'abc','def','ghi', 'jkl') == 'ghijkl'
    assert ex.mysum_bigger_than([2,3,4],[1,2,3], [4,5,6], [7,8,9]) == [4,5,6,7,8,9] 


def test_sum_numeric():
    assert ex.sum_numeric(10, 20, 'a', '30', 'bcd') == 60

def test_combine_dicts():
    dict1 = {'field1': 'value1'}
    dict2 = {'field2': 'value2'}
    dict3 = {'field2': 'value3'}
    dict4 = {'field1': 'value1', 'field2': ['value2', 'value3']}

    assert ex.combine_dicts([dict1, dict2, dict3]) == dict4