# Калькулятор доставки

def get_shipping_cost(quantity):
    total = 0
    for i in range(quantity):
        if i == 0:
            total += 1000
        else:
            total += 120
    return total


n = int(input())

print(get_shipping_cost(n))