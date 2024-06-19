# В поисках слов 😇

from collections import Counter

words = Counter([i.lower() for i in input().split()])

print(words.most_common(1)[0][0])