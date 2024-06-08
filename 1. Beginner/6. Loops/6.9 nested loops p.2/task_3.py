# Делители-1 🌶️

def get_count(number):
    result_count = 0
    result_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            result_count += 1
            result_sum += i

    return result_count, result_sum

a, b = int(input()), int(input())
maximals = {'count': 0, 'number': 0, 'sum': 0}


for i in range(a, b + 1):
    count, summ = get_count(i)
    if summ >= maximals['sum']:
        maximals['count'] = count
        maximals['sum'] = summ
        maximals['number'] = i

print(maximals['number'], maximals['sum'])