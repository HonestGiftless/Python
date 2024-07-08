# Xrange 🌶️
# Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.

class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.has_float = False
        if isinstance(self.start, int) and isinstance(self.end, int) and isinstance(self.step, int):
            self.range = iter(list(range(self.start, self.end, self.step)))
            self.has_float = False
        else:
            self.range = iter(iter(range(int(self.start * 100), int(self.end * 100), int(self.step * 100))))
            self.has_float = True

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.has_float:
            return next(self.range)
        else:
            return next(self.range) / 100