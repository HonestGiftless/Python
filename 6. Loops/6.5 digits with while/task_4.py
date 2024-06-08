# Все вместе

num = int(input())

score = 0
counter = 0
multy = 1
last_d = num % 10

while num > 0:
    last_digit = num % 10
    
    score += last_digit
    multy *= last_digit

    num //= 10

    counter += 1


first_n = last_digit
aver = score / counter
summ = first_n + last_d

print(score)
print(counter)
print(multy)
print(aver)
print(first_n)
print(summ)