# Beegeek
from re import search, match, fullmatch
import sys

bee_counter, geek_counter = 0, 0

for i in sys.stdin:
    i = i.strip()
    bee_test = search(r'(bee).*(bee)', i)
    geek_test = search(r'\b(geek)+\b', i)
    if bee_test:
        bee_counter += 1
    if geek_test:
        geek_counter += 1

print(bee_counter, geek_counter, sep='\n')