# Ревью кода-3

s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s = s + n
        
if s > 0:
    print(s)
else:
    print(0)