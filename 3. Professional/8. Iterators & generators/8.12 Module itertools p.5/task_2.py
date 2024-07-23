from itertools import permutations, combinations, combinations_with_replacement

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
result = list()

for i in range(1, len(wallet)):
    item = [i for i in set(combinations(wallet, i)) if sum(i) == 100]
    result.append(len(item))

print(sum(result))