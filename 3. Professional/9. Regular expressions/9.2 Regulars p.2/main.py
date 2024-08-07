# Регулярка для car, cat, cab
regex = r'ca[rtb]'

# Регулярка для символов шестнадцатеричной системы
regex = r'[0-9A-F]'

# Регулярка для Xxxxx
# X - любая буква латинского алфавита в произвольном регистре
# x - любая цифра
regex = r'[a-zA-Z]\d{4}'

# Регулярка по 5 условиям:
# первый символ — строчная латинская буква
# второй символ — произвольная цифра
# третий символ — строчная латинская буква
# четвертый символ — заглавная латинская буква
# пятый символ — заглавная латинская буква
regex = r'[a-z]\d[a-z][A-Z][A-Z]'

# Регулярка по 6 условиям:
# первый символ — произвольная цифра
# второй символ — строчная латинская гласная буква (a, e, i, o, u, y)
# третий символ — любой символ, кроме b, c, D, F
# четвертый символ — любой не пробельный символ
# пятый символ — любой символ, кроме заглавной латинской гласной буквы (A, E, I, O, U, Y)
# шестой символ — любой символ, кроме точки и запятой
regex = r'\d[aeiouy][^bcDF]\S[^AEIOUY][^.,]'

# Регулярка по 6 условиям:
# первый символ — цифра 1, 2 или 3
# второй символ — цифра 0, 1 или 2
# третий символ — цифра 1, 2 или строчная латинская буква x
# четвертый символ — цифра 0, 3 или латинская буква a в любом регистре
# пятый символ — строчная латинская буква x, s или u
# шестой символ — точка или запятая
regex = r'[1-3][0-2][12x][03aA][xsu][.,]'

# Регулярка по номеру телефона. Форматы:
# +7xxxxxxxxxx
# +7(xxx)xxxxxxx
# +7(xxx)-xxx-xx-xx
# +7 xxx xxx xx xx
regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}'

# Регулярка по датам. Форматы:
# DD.MM.YYYY
# DD/MM/YYYY
# YYYY.MM.DD
# YYYY/MM/DD
regex = r'\d{2}\.\d{2}\.\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2}|\d{4}/\d{2}/\d{2}'

# Регулярка по корректному времени HH:MM
regex = r'0[0-9]:[0-5][0-9]|1[0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]'