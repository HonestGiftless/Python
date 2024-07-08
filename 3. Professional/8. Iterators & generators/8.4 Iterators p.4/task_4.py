# Fibonacci
# Класс для генерации бесконечной последовательности чисел Фибоначчи

class Fibonacci:
    def __init__(self):
        self.value = 1
        self.prev = 1
        self.helpprev = 1
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1

        if 1 <= self.index <= 2:
            self.value = 1
        else:
            self.helpprev, self.prev = self.prev, self.value
            self.value = self.prev + self.helpprev
        
        return self.value