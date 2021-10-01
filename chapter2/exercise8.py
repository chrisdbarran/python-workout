def strsort(word: str):
    letters = []
    for letter in word:
        letters.append(letter)
    letters.sort()
    return ''.join(letters)


def strsort2(word: str):
    return ''.join(sorted(word))


def sort_words(line: str):
    return ', '.join(sorted(line.split()))


def last_word(words: str):
    return sorted(words.split())[-1]


def longest_word(words: str):
    return sorted(words.split(), key=len)[-1]
