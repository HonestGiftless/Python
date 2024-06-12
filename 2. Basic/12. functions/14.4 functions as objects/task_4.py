# Сортируй как хочешь

def name_sort(athlete):
    return athlete[0]

def age_sort(athlete):
    return athlete[1]

def height_sort(athlete):
    return athlete[2]

def width_sort(athlete):
    return athlete[3]

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
funcs = [name_sort, age_sort, height_sort, width_sort]
n = int(input())
athletes.sort(key=funcs[n-1])

for i in athletes:
    print(*i)