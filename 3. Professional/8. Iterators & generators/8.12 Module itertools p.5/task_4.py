# The problem of the backpack

from collections import namedtuple
from itertools import permutations, combinations, combinations_with_replacement

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

weight = int(input())
max_price = 0
result = list()

for i in range(1, len(items) + 1):
    test = combinations(items, i)

    for j in test:
        mass = sum(x.mass for x in j)
        if mass <= weight:
            result.append(j)

if len(result) > 0:
    curr_price = max(sum(j.price for j in i) for i in result)

    for i in result:
        price = sum(j.price for j in i)
        if price == curr_price:
            for j in sorted(i):
                print(j.name)
            break
else:
    print("Рюкзак собрать не удастся")