import operator
import sys


def gematria(wrds):
    gem_and_word = []

    for i in wrds:
        ords_sum = 0

        for j in i:
            ords_sum += ord(j.upper()) - ord("A") + 1

        gem_and_word.append((ords_sum, i))

    return [i[1].rstrip() for i in sorted(gem_and_word, key=operator.itemgetter(0, 1))]


words = [i for i in sys.stdin]

print(*gematria(words), sep="\n")
