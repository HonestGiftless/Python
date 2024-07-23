# password_gen()

from itertools import permutations, combinations, combinations_with_replacement, product

def password_gen():
    items = product(range(10), range(10), range(10))

    for i in items:
        yield f"{i[0]}{i[1]}{i[2]}"