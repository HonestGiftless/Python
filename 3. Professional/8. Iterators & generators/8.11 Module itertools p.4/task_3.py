# words group

from itertools import groupby

words = (i for i in input().split())
sorted_words = groupby(sorted(words, key=lambda item: (len(item), item)), key=len)

for i in sorted_words:
    print(i[0], '->', ", ".join(list(i[1])))