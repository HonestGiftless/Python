# verification()

import string

def verification(login, password, success, failure):
    errors = {0: 'в пароле нет ни одной буквы',
              1: 'в пароле нет ни одной заглавной буквы',
              2: 'в пароле нет ни одной строчной буквы',
              3: 'в пароле нет ни одной цифры'}
    
    password_none_symbol = list(filter(lambda item: item in string.ascii_letters or item.isdigit(), password))
    
    if all([i.isdigit() for i in password_none_symbol]):
        failure(login, errors[0])
    elif not any(filter(lambda item: item.isupper() and item.isalpha(), password_none_symbol)):
        failure(login, errors[1])
    elif not any(filter(lambda item: item.islower() and item.isalpha(), password_none_symbol)):
        failure(login, errors[2])
    elif all([i.isalpha() for i in password_none_symbol]):
        failure(login, errors[3])
    else:
        success(login)