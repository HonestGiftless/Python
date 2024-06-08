# Количество цифр

text = input()
cnt = 0

for i in text:
    if i in '0123456789':
        cnt += 1
    
print(cnt)