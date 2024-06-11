# Набор сообщений

buttons = {'1': '.,?!:',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
        '0': ' '}

message = input().upper()
counterList = []

for m in message:
    for key, value in buttons.items():
        for e in value:
            if m == e:
                index = value.index(e)
                counterList.append(key * (index + 1))
                
for i in counterList:
    print(i, end='')