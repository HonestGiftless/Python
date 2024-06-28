# minimum & maximum

function = input()
a, b = [int(i) for i in input().split()]
result = list()

for i in range(min(a, b), max(a, b) + 1):
    result.append(function.replace('x', f"({i})"))

print(f"Минимальное значение функции {function} на отрезке [{min(a, b)}; {max(a, b)}] равно", eval(min(result, key=lambda item: eval(item))))
print(f"Максимальное значение функции {function} на отрезке [{min(a, b)}; {max(a, b)}] равно", eval(max(result, key=lambda item: eval(item))))