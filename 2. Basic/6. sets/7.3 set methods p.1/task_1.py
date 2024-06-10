# Уникальные символы 1

n = int(input())
lst = []

for i in range(n):
    st = set(input().lower())
    lst.append(len(st))
    
print(*lst, sep='\n')