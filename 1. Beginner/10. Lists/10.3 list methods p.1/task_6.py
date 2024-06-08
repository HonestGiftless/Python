# Суммы двух

n = int(input())
l = []
l2 = []

for _ in range(n):
    num = int(input())
    l.append(num)
    
for i in range(1, len(l)):
    l2.append(l[i - 1] + l[i])
    
print(l2)