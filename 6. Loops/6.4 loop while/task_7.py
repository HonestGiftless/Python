# Ведьмаку заплатите чеканной монетой

n = int(input())

i = 0

while n >= 25:
    i += 1
    n -= 25
    
while n >= 10 and n < 25:
    i += 1
    n -= 10
    
while n >= 5 and n < 10:
    i += 1
    n -= 5
    
while n >= 1 and n < 5:
    i += 1
    n -= 1
    
print(i)