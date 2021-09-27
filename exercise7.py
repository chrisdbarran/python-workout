
def ubbi_dubbi(word: str):
    # every vowel prefaced with ub
    output = []
    vowels = 'aeiou'

    for letter in word:
        if letter in vowels:
            output.append('ub')
        output.append(letter)

    return ''.join(output) 