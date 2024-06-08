# max и min

num = int(input())

max_v = 0
min_v = 10

while num:
    last_d = num % 10
    
    if last_d >= max_v:
        max_v = last_d
        
    if last_d < min_v:
        min_v = last_d
        
    num //= 10
    
print('Максимальная цифра равна', max_v)
print('Минимальная цифра равна', min_v)