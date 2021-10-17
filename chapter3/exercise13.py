import operator
from typing import List
from collections import namedtuple

def format_sort_records(people: List[str]) ->str:
    output = []
    for person in sorted(people, key=operator.itemgetter(1,0)):
        output.append(f"{person[1]: <10} {person[0]: <10} {person[2]: >5.2f}")
    return output


def format_sort_named_tuple(people: List[namedtuple]) ->str:
    output = []
    for person in sorted(people, key=operator.attrgetter('last_name')):
        output.append(f"{person.last_name: <10} {person.first_name: <10} {person.journey_time: >5.2f}")
    return output