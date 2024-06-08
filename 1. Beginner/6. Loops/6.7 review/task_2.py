# Ревью кода-2 🌶️🌶️

mx = -10**6 - 1
s = 0

for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x > mx and x < 0:
        mx = x

if s < 0:
    print(s)
    print(mx)
else:
    print("NO")