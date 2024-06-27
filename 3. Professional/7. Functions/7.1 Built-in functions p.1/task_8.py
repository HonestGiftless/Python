# my_pow()

def my_pow(number):
    return sum([int(i[1])**int(i[0]) for i in enumerate(str(number), 1)])