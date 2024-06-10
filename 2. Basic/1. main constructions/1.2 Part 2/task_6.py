# Произведение чисел

n = int(input())
numbers = []
has_mult = False

for i in range(n):
    numbers.append(int(input()))

result = int(input())

for num in range(n):
    for j in range(n):
        if num != j:
            if numbers[num] * numbers[j] == result:
                has_mult = True
                break

if has_mult:
    print('ДА')
else:
    print('НЕТ')