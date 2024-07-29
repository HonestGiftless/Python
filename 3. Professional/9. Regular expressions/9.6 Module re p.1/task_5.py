# Popularity
from re import match, fullmatch
import sys

total = 0

for i in sys.stdin:
    i = i.strip()
    if fullmatch(r'\b(beegeek).*\1', i):
        total += 3
    elif match(r'beegeek', i) or fullmatch(r'\b.+(beegeek)', i):
        total += 2
    elif fullmatch(r'.+(beegeek).+', i):
        total += 1
    
print(total)