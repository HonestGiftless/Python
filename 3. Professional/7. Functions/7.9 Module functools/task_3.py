# Dima 🙃

from functools import lru_cache

@lru_cache(typed=True)
def ways(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        if n > 4:
            return ways(n - 4) + ways(n - 3) + ways(n - 1)
        elif n > 3:
            return ways(n - 3) + ways(n - 1)
        elif n > 1:
            return ways(n - 1)