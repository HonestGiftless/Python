# Напишите программу, которая считывает целое число и выводит для него на экран следующее и предыдущее целые числа в следующем формате:

# Следующее за числом <текущее число> число: <следующее число>
# Для числа <текущее число> предыдущее число: <предыдущее число>

n = int(input())

print('Следующее за числом', n, 'число:', n + 1)
print('Для числа', n, 'предыдущее число:', n - 1)