# is_prime()

def is_prime(number):
    if sum(i for i in range(1, number + 1) if number % i == 0) == number + 1:
        return True
    else:
        return False