import chapter3.exercise12 as ex

def test_most_repeating_word():
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    assert ex.most_repeating_word(words) == 'elementary'

def test_most_repeating_vowel():
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    assert ex.most_repeating_vowel(words) == 'elementary'