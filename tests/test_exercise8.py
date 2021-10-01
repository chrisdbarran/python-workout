import chapter2.exercise8 as ex
import pytest

@pytest.fixture
def words():
    return """ Python programmers are constantly dealing with text Whether 
    it’s because we’re reading from files, displaying things on the screen, or just using dicts,
    strings are a data type with which we’re likely familiar from other languages"""

def test_strsort():
    assert ex.strsort('cba') == 'abc'
    assert ex.strsort('abcdefg') == 'abcdefg'
    assert ex.strsort('qazwsxedcrfvtgbyhnujmiklop') == 'abcdefghijklmnopqrstuvwxyz'

def test_strsort2():
    assert ex.strsort2('cba') == 'abc'
    assert ex.strsort2('abcdefg') == 'abcdefg'
    assert ex.strsort2('qazwsxedcrfvtgbyhnujmiklop') == 'abcdefghijklmnopqrstuvwxyz'

def test_sort_words():
    assert ex.sort_words("Tom Dick Harry") == "Dick, Harry, Tom"

def test_last_word(words):
    assert ex.last_word(words) == "with"

def test_longest_word(words):
    assert ex.longest_word(words) == "programmers"
