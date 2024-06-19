# Статистика длин слов

from collections import Counter

words = Counter([len(i) for i in input().split()])
needed = sorted(words.items(), key=lambda item: item[1])

for i in needed:
    print(f"Слов длины {i[0]}: {i[1]}")