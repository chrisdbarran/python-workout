import string


def pig_latin(word: str) -> str:
    if word[0] in 'aeiou':
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"


def pig_latin_ternary(word: str) -> str:
    return f"{word}way" if word[0] in 'aeiou' else f"{word[1:]}{word[0]}ay"


def pig_latin_capitalised(word: str) -> str:
    return pig_latin(word).capitalize() if word[0].isupper() else pig_latin(word)


def pig_latin_punctuation(word: str) -> str:
    if word[-1] in string.punctuation:
        return f"{pig_latin_capitalised(word[:-1])}{word[-1]}"
    return pig_latin_capitalised(word)


def pig_latin_two_vowels(word: str) -> str:
    vowels = {letter for letter in word if letter in 'aeiouAEIOU'}
    return f"{word}way" if len(vowels) > 1 else f"{word[1:]}{word[0]}ay"


if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"Pig Latin: {pig_latin(word)}")
