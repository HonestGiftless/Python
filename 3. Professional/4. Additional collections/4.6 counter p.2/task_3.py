# В поисках слов 🥳

from collections import Counter

words = Counter([i.lower() for i in input().split()])
rst = sorted([i for i in words if words[i] == words.most_common(1)[0][1]], reverse=True)

print(rst[0])