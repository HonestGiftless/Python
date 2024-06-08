# Наибольшие числа 🌶️🌶️

n = int(input())

max_val = -1
sec_max = -1

for i in range(n):
    num = int(input())
    if num > max_val:
        sec_max = max_val
        max_val = num
    elif num > sec_max:
        sec_max = num
        
print(max_val)
print(sec_max)