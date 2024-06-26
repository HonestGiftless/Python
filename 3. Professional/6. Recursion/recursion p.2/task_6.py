# Rapid pow

def get_fast_pow(a, n):
    if n < 0:
        return get_fast_pow(1 / a, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return get_fast_pow(a * a, n // 2)
    else:
        return a * get_fast_pow(a, n - 1)