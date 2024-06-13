# Функция filter_anagrams()

def filter_anagrams(word, words):
    result = list()
    dct_count = dict()

    for i in word:
        dct_count[i] = 0
    for i in word:
        dct_count[i] += 1

    for i in words:
        if len(i) == len(word):
            counter = dict()
            for j in i:
                counter[j] = 0
            for j in i:
                counter[j] += 1

            if counter == dct_count:
                result.append(i)

    return result