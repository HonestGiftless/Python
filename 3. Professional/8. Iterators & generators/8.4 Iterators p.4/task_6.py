# DictItemsIterator
# Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.

class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.value = iter(self.data)
        self.key = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1

        if self.index >= len(self.data):
            raise StopIteration
        else:
            self.key = next(self.value)
            return self.key, self.data[self.key]