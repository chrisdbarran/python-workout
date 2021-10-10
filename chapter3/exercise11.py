from typing import List, Dict
from operator import itemgetter


def alphabetize_names(names: List[Dict]) -> List[Dict]:
    return sorted(names, key=itemgetter('last', 'first'))

def sort_absolute(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=abs)

def vowel_sort(words: List[str]) -> List[str]:
    return sorted(words, key=lambda word:  len([ letter for letter in word if letter in 'aeiouAEIOU']))

def number_sort(lists_of_numbers: List[List[int]]) -> List[List[int]]:
    return sorted(lists_of_numbers, key=sum)