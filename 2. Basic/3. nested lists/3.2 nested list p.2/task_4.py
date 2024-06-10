# Треугольник Паскаля 2

n = int(input())
P=[]

for i in range(0,n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j!=i:
            row[j]=P[i-1][j-1]+P[i-1][j]
    P.append(row)

for r in P:
    print(*r)