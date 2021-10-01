import chapter1.exercise2 as ex


def test_mysum_returns_zero_no_args():
    # arrange
    # act
    # assert
    assert ex.mysum() == 0


def test_mysum_returns_sum():
    # arrange
    # act
    # assert
    assert ex.mysum(1, 1) == 2

def test_mysum_adds_list():
    assert ex.mysum(*[1, 1]) == 2


def test_mysum_with_start():
    assert ex.mysum_with_start([1, 2, 3], 4) == 10


def test_mysum_with_start_minus():
    assert ex.mysum_with_start([1, 2, 3], -4) == 2


def test_average_of_numbers():
    assert ex.average([1, 2, 3]) == 2
    assert ex.average([3, 1, 6]) == 3.33


def test_words():
    assert ex.words(["This", "is", "a", "Test"]) == (1, 4, 2.75)


def test_sum_objects():
    assert ex.sum_objects([1, "1"]) == 2
    assert ex.sum_objects([1, 1.1]) == 2
    assert ex.sum_objects([1, 1.6]) == 2
    assert ex.sum_objects([1, "2", "F"]) == 3
