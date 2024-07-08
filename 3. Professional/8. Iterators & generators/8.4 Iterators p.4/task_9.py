# RandomNumbers
# Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left до right включительно, а затем возбуждать исключение StopIteration.

from random import choice

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.values = list(range(self.left, self.right + 1))
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1

        if self.index > self.n:
            raise StopIteration
        else:
            return choice(self.values)