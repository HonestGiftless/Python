# BEEGEEK

def is_prime(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False

def is_valid_password(password):
    x = password.split(':')
    total = 0

    if len(x) == 3:
        total += 1
    if x[0] == x[0][::-1]:
        total += 1
    if is_prime(int(x[1])) == True:
        total += 1
    if int(x[2]) % 2 == 0:
        total += 1
    
    if total == 4:
        return True
    else:
        return False
            

password = input()

print(is_valid_password(password))