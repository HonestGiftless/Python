# ФИО

def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)