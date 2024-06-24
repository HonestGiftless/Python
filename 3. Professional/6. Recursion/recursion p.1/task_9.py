# print_digits() 😎

def print_digits(number):
    if len(str(number)) > 0:
        print(str(number)[0])
        print_digits(str(number)[1:])