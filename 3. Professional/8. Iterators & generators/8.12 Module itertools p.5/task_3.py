from itertools import permutations, combinations, combinations_with_replacement

wallet = [100, 50, 20, 10, 5]
counter = 0

for i in range(1, 21):
    item = set(combinations_with_replacement(wallet, i))
    for j in item:
        if sum(j) == 100:
            counter += 1

print(counter)