# Класс Numbers

class Numbers:
    def __init__(self) -> None:
        self.items = []

    def add_number(self, number):
        self.items.append(number)

    def get_even(self):
        return [i for i in self.items if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.items if i % 2 != 0]