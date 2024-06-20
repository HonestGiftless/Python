# Булочный магнат

from collections import ChainMap, Counter, defaultdict

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

products = ChainMap(bread, meat, sauce, vegetables, toppings)
needed = Counter(input().split(','))
result = defaultdict(int)
total = 0

for k, v in needed.items():
    result[k] = v * products[k]

maximal_length = len(max(result.items(), key=lambda item: len(item[0]))[0])
total_max = 0

result = sorted(result.items(), key=lambda item: item[0])

for i in result:
    res_text = f"{i[0].ljust(maximal_length)} x {needed[i[0]]}"
    print(res_text)
    total += i[1]
    if len(i[0]) == maximal_length:
        total_max = len(res_text)

itog = f"ИТОГ: {total}р"

if len(itog) > total_max:
    total_max = len(itog)

print("-" * total_max, itog, sep='\n')