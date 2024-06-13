# Корпоративная почта 🌶️

digits = '0123456789'
names = list()

for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)

for _ in range(int(input())):
    name = input()
    counter = 0
    while name in names:
        counter += 1
        name = name.rstrip(digits) + str(counter)
    names.append(name)
    print(f"{name}@beegeek.bzz")