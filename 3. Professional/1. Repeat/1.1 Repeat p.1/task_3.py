# Функция is_valid()

def is_valid(string):
    if 4 <= len(string) <= 6 and string.isdigit() and " " not in string:
        return True
    else:
        return False