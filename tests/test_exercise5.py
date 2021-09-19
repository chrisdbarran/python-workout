import exercise5 as ex


def test_pig_latin_non_vowel():
    assert ex.pig_latin("computer") == "omputercay"


def test_pig_latin_vowel():
    assert ex.pig_latin("air") == "airway"


def test_pig_latin_ternary():
    assert ex.pig_latin_ternary("computer") == "omputercay"
    assert ex.pig_latin_ternary("air") == "airway"


def test_pig_latin_capitalised():
    assert ex.pig_latin_capitalised("Computer") == "Omputercay"
    assert ex.pig_latin_capitalised("computer") == "omputercay"


def test_pig_latin_punctuation():
    assert ex.pig_latin_punctuation("Computer") == "Omputercay"
    assert ex.pig_latin_punctuation("computer") == "omputercay"
    assert ex.pig_latin_punctuation("Computer.") == "Omputercay."
    assert ex.pig_latin_punctuation("computer!") == "omputercay!"


def test_pig_latin_two_vowels():
    assert ex.pig_latin_two_vowels("wine") == "wineway"
    assert ex.pig_latin_two_vowels("wind") == "indway"