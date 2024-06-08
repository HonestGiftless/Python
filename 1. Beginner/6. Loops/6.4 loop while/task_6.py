# Количество пятерок

assessment = int(input())

i = 0

while assessment >= 0 and assessment <= 5:
    if assessment == 5:
        i += 1
    assessment = int(input())

print(i)