# Биномиальный коэффициент 🌶️

from math import factorial

def compute_binom(n, k):
    x = factorial(n) / (factorial(k) * (factorial(n - k)))
    return int(x)

n = int(input())
k = int(input())

print(compute_binom(n, k))