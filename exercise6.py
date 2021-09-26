import re
from typing import List
import exercise5 as ex5

def pl_sentence(sentence: str):
    words = sentence.split()
    pl_words = map(ex5.pig_latin, words)
    return ' '.join(pl_words)

def nonsense(filename: str):
    output = []
    with open(filename, encoding='utf8') as file:
        for i in range (0,10):
            words = file.readline().split()
            output.append(words[i])
        return ' '.join(output)

def transpose(provided: List[str]):
    output = []
    for strings in provided:
        parts = strings.split()
        output.append(parts)
    result = []

    for j in range(len(output[0])):
        temp = []
        for (i, _) in enumerate(output):
            temp.append(output[i][j])
        result.append(' '.join(temp))
    return result


def apache(filename: str):
    log_pattern = r'((?:[0-9]{1,3}\.){3}[0-9]{1,3}) - - (\[.*\]) (\".*\") (\d+) (\d+)'
    with open(filename, encoding='utf8') as file:
        for line in file.readlines():
            z = re.match(log_pattern, line)
            if z:
                groups = z.groups()
                if groups[3] == '404':
                    return groups[0]
    return None


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(f"Pig Latin: {pl_sentence(sentence)}")
