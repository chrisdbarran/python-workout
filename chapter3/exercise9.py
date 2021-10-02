from typing import Iterable


def firstlast(iterable: Iterable):
    return iterable[:1] + iterable[-1:]

def even_odd_sums(numbers):
    evens = [num for (i, num) in enumerate(numbers) if i % 2 == 0 ]
    odds = [num for (i, num) in enumerate(numbers) if i % 2 > 0 ]
    return [sum(evens), sum(odds)]

def plus_minus(numbers):
    total = numbers[:1][0]
    for (i, num) in enumerate(numbers[1:]):
        if(i%2):
            total -= num
        else:
            total += num
    return total
