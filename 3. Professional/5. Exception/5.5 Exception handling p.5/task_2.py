# is_good_password() 🐍

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
                raise DigitError()
        else:
            raise LetterError()
    else:
        raise LengthError()
