# Самый частотный символ

s = input()
cnt = 0
largest = 0

for i in s:
    if s.count(i) >= cnt:
        cnt = s.count(i)
        largest = i
        
print(largest)