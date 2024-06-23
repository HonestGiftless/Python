# Уж лучше матрицы 😐

class LengthError(Exception):
    pass

class LetterError(Exception):
    pass

class DigitError(Exception):
    pass

def is_good_password(string):
    if len(string) >= 9:
        if len([i for i in string if i.isupper() and i.isalpha()]) > 0 and len([i for i in string if i.islower() and i.isalpha()]) > 0:
            if len([i for i in string if i.isdigit()]) > 0:
                return True
            else:
                raise DigitError("DigitError")
        else:
            raise LetterError("LetterError")
    else:
        raise LengthError("LengthError")

password = input()

while True:
    try:
        if is_good_password(password):
            print("Success!")
            break
    except Exception as e:
        print(e)
        password = input()