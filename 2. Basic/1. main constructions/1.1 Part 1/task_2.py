# Индекс массы тела

def switch(imt):
    if (18.5 <= imt <= 25):
        print('Оптимальная масса')
    elif (imt < 18.5):
        print('Недостаточная масса')
    else:
        print('Избыточная масса')

w, h = float(input()), float(input())
imt = w / (h**2)

switch(imt)