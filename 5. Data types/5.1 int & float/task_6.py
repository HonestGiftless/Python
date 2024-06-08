# Первая цифра после точки

num = float(input())
num = int((num - int(num)) * 10)

print(num)