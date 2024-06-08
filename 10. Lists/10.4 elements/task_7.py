# Negatives, Zeros and Positives

n = int(input())
l, l2, l3, l4 = [], [], [], []

for _ in range(n):
    num = int(input())
    l.append(num)

for i in l:
    if i < 0:
        l2.append(i)
    if i == 0:
        l3.append(i)
    if i > 0:
        l4.append(i)

l_e = l2 + l3 + l4

print(*l_e, sep='\n')