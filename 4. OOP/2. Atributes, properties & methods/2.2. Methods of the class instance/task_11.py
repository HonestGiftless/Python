# Класс TextHandler

class TextHandler:
    def __init__(self):
        self.text = []

    def add_words(self, text):
        self.text.extend(text.split())
    
    def get_shortest_words(self):
        return [i for i in self.text if len(i) == len(min(self.text, key=len))]
    
    def get_longest_words(self):
        return [i for i in self.text if len(i) == len(max(self.text, key=len))]