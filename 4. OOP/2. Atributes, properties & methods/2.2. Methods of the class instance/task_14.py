# Класс Wordplay

class Wordplay:
    def __init__(self, words=[]) -> None:
        self.words = list(words)
        self.only_result = []
        self.avoid_result = []

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]

    def only(self, *args):
        for word in self.words:
            if set(word) == args:
                self.only_result.append(word)
            else:
                if all([True if i in args else False for i in word]):
                    self.only_result.append(word)
        
        return self.only_result

    def avoid(self, *args):
        for word in self.words:
            if not any([True if i in args else False for i in word]):
                self.avoid_result.append(word)

        return self.avoid_result