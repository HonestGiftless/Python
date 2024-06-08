# Упорядоченные цифры 🌶️

num = input()
counter = 0

for i in range(1, len(num)):
    if int(num[i]) <= int(num[i - 1]):
        counter += 1

if counter == len(num) - 1:
    print("YES")
else:
    print("NO")