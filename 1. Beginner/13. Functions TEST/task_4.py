#  Число словами 🌶️

def number_to_words(num):
    dig = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    dec = ['',  'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
           'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    teen = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
            'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    x = ''
    if n == 0:
        return 'ноль'
    if (10 < n % 100 < 20):
        x += teen[n % 10]
    else:
        d = dec[n % 100 // 10]
        x += d + (d and ' ' or '') + dig[n % 10]
    return x

n = int(input())

print(number_to_words(n))