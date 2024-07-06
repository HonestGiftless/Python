# Dima 🙂

import sys
from functools import lru_cache

@lru_cache(typed=True)
def sorting(arg):
    return "".join(sorted(arg))

result = [sorting(i.strip()) for i in sys.stdin]

print(*result, sep='\n')