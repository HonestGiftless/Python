# Correct dates

from datetime import date

def is_correct(day, month, year, items):
    try:
        my_date = date(year, month, day)
        items.append('Корректная')
    except ValueError:
        items.append('Некорректная')

my_date = input()
items = list()

while my_date != 'end':
    new_date = my_date.split('.')
    is_correct(int(new_date[0]), int(new_date[1]), int(new_date[2]), items)
    my_date = input()

print(*items, sep='\n')
print(items.count('Корректная'))