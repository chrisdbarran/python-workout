from typing import Sequence
from collections import Counter

def most_repeating_word(words: Sequence[str]) -> str:
    return max(words, key=most_repeating_letter_count)

def most_repeating_letter_count(word: str) -> int:
    return max(Counter(word).values())