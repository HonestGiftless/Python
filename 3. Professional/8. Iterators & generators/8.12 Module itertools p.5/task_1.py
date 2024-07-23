# Permutations

from itertools import permutations, combinations, combinations_with_replacement

text = input()

for i in sorted(set(permutations(text))):
    print("".join(i))