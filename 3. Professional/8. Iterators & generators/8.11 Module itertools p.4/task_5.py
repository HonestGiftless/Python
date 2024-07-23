# group_anagrams()

from itertools import groupby

def group_anagrams(words: list):
    '''Функция для составления групп анаграмм слов из списка'''
    groupped_words = groupby(sorted(words, key=sorted), key=sorted)

    for i in groupped_words:
        yield tuple(i[1])