# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

age = int(input())

if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 24 <= age <= 59:
    print('зрелость')
if 60 <= age:
    print('старость')