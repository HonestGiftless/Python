# count_occurences()

def count_occurences(word, words):
    return [i.lower() for i in words.split()].count(word.lower())