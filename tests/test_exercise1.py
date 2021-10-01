import chapter1.exercise1 as ex1


def test_answer_returns_int():
    # arrange
    # act
    target = ex1.get_answer()
    # assert
    assert isinstance(target, int)


def test_check_too_high():
    # arrange
    # act
    response = ex1.check(99, 55)
    # assert
    assert (True, "Too high!") == response


def test_check_too_low():
    # arrange
    # act
    response = ex1.check(44, 55)
    # assert
    assert (True, "Too low!") == response


def test_check_just_right():
    # arrange
    # act
    response = ex1.check(55, 55)
    # assert
    assert (False, "Just right!") == response
