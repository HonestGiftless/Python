# Функция convert()

import string

lower_case_alph = string.ascii_lowercase
upper_case_alph = string.ascii_uppercase

def convert(string):
    lower_counter = 0
    upper_counter = 0

    for s in string:
        if s in lower_case_alph:
            lower_counter += 1
        elif s in upper_case_alph:
            upper_counter += 1

    if lower_counter > upper_counter or lower_counter == upper_counter:
        return string.lower()
    else:
        return string.upper()