import random


def random_string(characters, length):
    result = []
    for i in range(length):
        while True:
            char = random.choice(characters)
            if i > 0 and result[i - 1] == char:
                continue
            break
        result.append(char)
    return "".join(result)
