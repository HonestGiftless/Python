class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1
            return self.low - 1
        
class EvenNumbers:
    def __init__(self, begin):
        self.begin = begin + begin % 2

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.begin
        self.begin += 2
        return value
    
class StringWrapper:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.text):
            raise StopIteration
        return self.symbol + self.text[self.index] + self.symbol
    
class Factorials:
    def __init__(self):
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value
