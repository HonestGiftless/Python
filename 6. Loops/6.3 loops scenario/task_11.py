# Последовательность Фибоначчи 🌶️

n = int(input())
lst = [1]

for i in range(n-1):
    if i == 0:
        lst.append(1)
    elif i == 1:
        lst.append(sum(lst))
    else:
        lst.append(lst[-1] + lst[-2])
        
print(*lst)