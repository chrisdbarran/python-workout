import chapter3.exercise13 as ex
from collections import namedtuple

Person = namedtuple('Person',['first_name', 'last_name', 'journey_time'])

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def test_format_sort_records():
    sorted_people = ex.format_sort_records(PEOPLE)
    validate_people(sorted_people)


TUPLE_PEOPLE = [ Person(first_name='Donald', last_name='Trump', journey_time=7.85),
                 Person(first_name='Vladimir', last_name='Putin', journey_time=3.626),
                 Person(first_name='Jinping', last_name='Xi', journey_time=10.603)]


def format_sort_named_tuple():
    sorted_people = ex.format_sort_named_tuple(TUPLE_PEOPLE)
    validate_people(sorted_people)

def validate_people(sorted_people: str):
    print("\n".join(sorted_people))
    assert sorted_people[0] == "Putin      Vladimir    3.63"
    assert sorted_people[1] == "Trump      Donald      7.85"
    assert sorted_people[2] == "Xi         Jinping    10.60"
