# Стоимость строки

txt = input()

price_kop = len(txt) * 60
price_rub = price_kop // 100
div = price_kop % 100

print(price_rub, 'р.', div, 'коп.')