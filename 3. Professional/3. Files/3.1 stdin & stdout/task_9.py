# The Guru of Progressions

import sys

def is_ariphmetic(numbers):
    d = numbers[1] - numbers[0]
    counter = 0

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] == d:
            counter += 1

    if counter == len(numbers) - 1:
        return True
    else:
        return False
    
def is_geometric(numbers):
    d = numbers[1] // numbers[0]
    counter = 0

    for i in range(1, len(numbers)):
        if numbers[i] // numbers[i - 1] == d:
            counter += 1

    if counter == len(numbers) - 1:
        return True
    else:
        return False
    

data = [int(i.strip('\n')) for i in sys.stdin]

if is_ariphmetic(data):
    print("Арифметическая прогрессия")
elif is_geometric(data):
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")