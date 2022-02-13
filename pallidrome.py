"""create a pallidrome."""

import random

alphabet = 'abcdefghijklmopqrstuvwxyz'


def main():
    len_word = random.randint(0, 10)
    result = ''
    for _ in range(len_word):
        result += alphabet[random.randint(0, len(alphabet) - 1)]
    len_result = len(result)
    for i in range(len_result):
        result += result[(len_result - 1) - i]
    return result


print(main())
