# Вид треугольника

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')