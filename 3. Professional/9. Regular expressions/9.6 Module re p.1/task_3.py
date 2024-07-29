# Identical syllables
from re import search, match, fullmatch
import sys

for i in sys.stdin:
    i = i.strip()
    test = fullmatch(r'(\w+)\1', i)
    if test:
        print(i)