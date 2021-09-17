import sys
from typing import List, Tuple, Any


def mysum(*args) -> int:
    output = 0
    for arg in args:
        output += int(arg)
    return output

def mysum_with_start(numbers: List[int], start: int ) -> int:
    numbers.append(start)
    return mysum(*numbers)


def average(numbers: List[int]) -> float:
    return round(mysum(*numbers) / len(numbers), 2)


def words(words: List[str]) -> Tuple[int, int, int]:
    word_lengths = [len(word) for word in words]
    return (min(word_lengths), max(word_lengths), average(word_lengths))


def sum_objects(objects: List[Any]) -> int:
    integers = []
    for obj in objects:
        try:
            integers.append(int(obj))
        except ValueError:
            pass
    return mysum(*integers)


if __name__ == "__main__":
    total = mysum(*sys.argv[1:])
    print(total)
