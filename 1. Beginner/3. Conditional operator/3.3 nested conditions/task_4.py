# Количество дней

month = int(input())

if month == 2:
    print('28')
else:
    print(30 + (month + month // 8) % 2)