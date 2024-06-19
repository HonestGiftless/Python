# The Zen of Python

from collections import Counter

counter = Counter()

with open("pythonzen.txt", 'r', encoding='utf-8') as file:
    text = [i.strip() for i in file.readlines()]
    
    for i in text:
        i = list(filter(str.isalpha, i.lower()))
        if len(i) > 0:
            counter.update(i)
    
counter = sorted(counter.items(), key=lambda item: item[0])

for i in counter:
    print(f"{i[0]}: {i[1]}")