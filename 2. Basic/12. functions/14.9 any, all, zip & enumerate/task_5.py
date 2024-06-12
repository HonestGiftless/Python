# Интересные числа

def is_interesting(lst):
    result = list()
    for i in lst:
        if '0' in str(i):
            continue
        else:
            counter = 0
            for j in str(i):
                if i % int(j) == 0:
                    counter += 1
            if counter == len(str(i)):
                result.append(i)

    return result

start_point, end_point = int(input()), int(input())
numbers = list()

for i in range(start_point, end_point + 1):
    numbers.append(i)

x = is_interesting(numbers)
print(*x)