import chapter3.exercise11 as ex

PEOPLE = [{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'},
 {'first':'Peter', 'last':'Putin',
    'email':'peter@kremvax.ru'},
 ]

TEST_PEOPLE = [{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
  {'first':'Peter', 'last':'Putin',
    'email':'peter@kremvax.ru'},
  {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'},
  {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'}
 ]


def test_alphabetize_names():
    assert ex.alphabetize_names(PEOPLE) == TEST_PEOPLE

def test_sort_absolute():
    assert ex.sort_absolute([-7, -3, -20, 5, 3, 0, 1, -1]) == [0 , 1, -1, -3, 3, 5, -7, -20 ]

def test_vowel_sort():
    words = "Now consider that when we define a function using".split(' ')
    expected = ["Now", "that", "when", "we", "a", "using", "consider", "define", "function"]
    assert ex.vowel_sort(words) == expected

def test_number_sort():
    lists = [[1, 2, 3] ,[] , [4, -9], [9, 8, 7, 5, 4, 3]]
    assert ex.number_sort(lists) == [[4, -9], [], [1, 2, 3], [9, 8, 7, 5, 4, 3]]
   