# Функция get_biggest() 🌶️🌶️

def get_biggest(numbers):
    if numbers:
        s = ""
        max_length = len(str(max(numbers)))
        numbers = sorted([str(i) for i in numbers], reverse=True, key=lambda item: item * max_length)
        return int(s.join(numbers))
    
    return -1