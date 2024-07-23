# Number systems

from itertools import permutations, combinations, combinations_with_replacement, product

n, m = int(input()), int(input())
yo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'][:n]
items = product(yo, repeat=m)

for i in items:
    print("".join(i), end=' ')