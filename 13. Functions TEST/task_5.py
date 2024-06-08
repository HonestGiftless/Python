# Искомый месяц

def get_month(language, number):
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    if language == 'ru':
        return ru[number]
    else:
        return en[number]

lan = input()
num = int(input())

print(get_month(lan, num))