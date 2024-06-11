# Покупки в интернет-магазине 🌶️

result = dict()

n = int(input())

for i in range(n):
    purchase = input().split()

    if purchase[0] not in result.keys():
        result[purchase[0]] = {purchase[1]: int(purchase[2])}
    else:
        if purchase[1] not in result[purchase[0]].keys():
            result[purchase[0]][purchase[1]] = int(purchase[2])
        else:
            result[purchase[0]][purchase[1]] += int(purchase[2])

for k, v in result.items():
    result[k] = dict(sorted(v.items()))

result = dict(sorted(result.items()))

for k, v in result.items():
    print(f"{k}:")
    for key, value in v.items():
        print(key, value)