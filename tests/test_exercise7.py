import exercise7 as ex

def test_ubbi_dubbi():
    assert ex.ubbi_dubbi("milk") == "mubilk"
    assert ex.ubbi_dubbi("program") == "prubogrubam"
    assert ex.ubbi_dubbi("octopus") == "uboctubopubus"
    assert ex.ubbi_dubbi("elephant") == "ubelubephubant"
    assert ex.ubbi_dubbi("soap") == "suboubap"