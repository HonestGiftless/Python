# Square
# Класс для генерации последовательности квадратов из n чисел

class Square:
    def __init__(self, n):
        self.n = n
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.value = self.index ** 2
        if self.index > self.n:
            raise StopIteration
        else:
            self.index += 1
            return self.value