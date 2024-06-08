# Одинаковые цифры

num = int(input())
flag = True

while num > 9:
    last = num % 10
    num = num // 10  
    sec = num % 10  
    if last != sec:
        flag = False
    
if flag:
    print('YES')
else:
    print('NO')
                     