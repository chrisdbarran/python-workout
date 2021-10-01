
def ubbi_dubbi(word: str):
    # every vowel prefaced with ub
    output = []
    vowels = 'aeiouAEIOU'

    for letter in word:
        if letter in vowels:
            output.append('ub')
        output.append(letter)

    return ''.join(output)

def ubbi_dubbi_capitalize(word: str):

    return ubbi_dubbi(word).capitalize() if word[0].isupper() else ubbi_dubbi(word)