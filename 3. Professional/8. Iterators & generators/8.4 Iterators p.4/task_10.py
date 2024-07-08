# Alphabet 🌶️
# Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв

class Alphabet:
    def __init__(self, language):
        self.language = language
        self.symbols = {'ru': [chr(i) for i in range(1072, 1104)], 'en': [chr(i) for i in range(97, 123)]}
        self.current_symbols = iter(self.symbols[self.language])

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self.current_symbols)
        except StopIteration:
            self.current_symbols = iter(self.symbols[self.language])
            return next(self.current_symbols)