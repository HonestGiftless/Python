# Популяция

m = float(input())
p = float(input())
n = int(input())

for i in range(n):
    if i == 0:
        print(i + 1, m)
    else:
        percent = m / 100 * p
        m += percent
        print(i + 1, m)