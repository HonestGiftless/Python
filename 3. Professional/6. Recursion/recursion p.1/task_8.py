# print_digits() 😉

def print_digits(number):
    if number > 0:
        print(number % 10)
        print_digits(number // 10)