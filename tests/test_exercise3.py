import chapter1.exercise3 as ex


def test_before_and_after():
    # arrange
    # act
    # assert
    assert ex.before_and_after(1234.5678, 2, 3) == 34.567


def test_add_floats():
    assert ex.add_floats("54.23", "34.66") == 88.89
    assert ex.add_floats("0.1", "0.2") == 0.3
