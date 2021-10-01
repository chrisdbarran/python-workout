import chapter2.exercise7 as ex

def test_ubbi_dubbi():
    assert ex.ubbi_dubbi("milk") == "mubilk"
    assert ex.ubbi_dubbi("program") == "prubogrubam"
    assert ex.ubbi_dubbi("octopus") == "uboctubopubus"
    assert ex.ubbi_dubbi("elephant") == "ubelubephubant"
    assert ex.ubbi_dubbi("soap") == "suboubap"


def test_ubbi_dubbi_capitalize():
    assert ex.ubbi_dubbi_capitalize("Milk") == "Mubilk"
    assert ex.ubbi_dubbi_capitalize("program") == "prubogrubam"
    assert ex.ubbi_dubbi_capitalize("Octopus") == "Uboctubopubus"
    assert ex.ubbi_dubbi_capitalize("elephant") == "ubelubephubant"
    assert ex.ubbi_dubbi_capitalize("soap") == "suboubap"