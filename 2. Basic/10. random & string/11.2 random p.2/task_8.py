# Генератор паролей 1

import random
import string

def generate_password(length):
    password = ''
    letters = string.ascii_letters

    for i in range(length):
        letter = random.choice(letters)
        while letter in 'lI1oO0':
            letter = random.choice(letters)
        password += letter

    return password

def generate_passwords(count, length):
    return [generate_password(length) for i in range(count)]

print(*generate_passwords(int(input()), int(input())), sep='\n')