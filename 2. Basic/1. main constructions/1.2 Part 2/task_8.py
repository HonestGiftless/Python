# Камень, ножницы, бумага, ящерица, Спок 🌶️

data = {'камень': 'ящерица ножницы',
        'ножницы': 'ящерица бумага',
        'бумага': 'камень спок',
        'ящерица': 'спок бумага',
        'спок': 'ножницы камень'}

choice1 = input().lower()
choice2 = input().lower()

if choice2 in data[choice1]:
    print('Тимур')
elif choice1 in data[choice2]:
    print('Руслан')
else:
    print('ничья')