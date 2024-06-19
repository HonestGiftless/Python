# scrabble()

from collections import Counter

def scrabble(symbols, word):
    symbols = Counter(symbols.lower())
    word = Counter(word.lower())

    symbols.subtract(word)
    if any([True if symbols[i] < 0 else False for i in symbols]):
        return False
    else:
        return True