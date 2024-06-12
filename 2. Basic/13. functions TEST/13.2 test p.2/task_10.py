# Гематрия слова

words = [input() for i in range(int(input()))]
words = sorted(words)
dct = dict()

for word in words:
    total = 0
    for j in range(len(word)):
        total += ord(word[j].upper()) - ord("A")
    dct[word] = total

dct = dict(sorted(dct.items(), key=lambda item: item[1]))

for k in dct.keys():
    print(k)