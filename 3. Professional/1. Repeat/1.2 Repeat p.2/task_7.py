# Схожие слова

def get_vowels_count(word):
    counter = 0

    for i in word:
        if i in "ауоыиэяюёе":
            counter += 1
    
    return counter

def get_vowels_index(word):
    result = list()

    for i in range(len(word)):
        if word[i] in "ауоыиэяюёе":
            result.append(i)

    return result

start_word = input()
start_vowel_count = get_vowels_count(start_word)
start_vowel_indexes = get_vowels_index(start_word)

words = [input().lower() for i in range(int(input()))]

result = list()

for word in words:
    counter = 0

    count = get_vowels_count(word)
    indexes = get_vowels_index(word)

    if count == start_vowel_count and indexes == start_vowel_indexes:
        result.append(word)

print(*result, sep='\n')