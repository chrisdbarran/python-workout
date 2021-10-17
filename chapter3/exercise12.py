from typing import Sequence
from collections import Counter

def most_repeating_word(words: Sequence[str]) -> str:
    return max(words, key=most_repeating_letter_count)

def most_repeating_letter_count(word: str) -> int:
    return max(Counter(word).values())

def most_repeating_vowel(words: Sequence[str]) -> str:
    return max(words, key=most_repeating_vowel_count)

def most_repeating_vowel_count(word: str) -> int:
    counts = Counter(word)
    vowels = {key: counts[key] for key in counts.keys() & {'a','e','i','o','u'}}
    return max(vowels.values())