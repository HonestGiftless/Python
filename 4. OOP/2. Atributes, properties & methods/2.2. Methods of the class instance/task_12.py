# Класс Todo

class Todo:
    def __init__(self):
        self.things = []
        self.minimum = 10
        self.maximum = 0

    def add(self, name, priority):
        self.things.append((name, priority))
        if priority < self.minimum:
            self.minimum = priority
        elif priority > self.maximum:
            self.maximum = priority

    def get_by_priority(self, n):
        return [do[0] for do in self.things if do[1] == n]
    
    def get_low_priority(self):
        return [do[0] for do in self.things if do[1] == self.minimum]

    def get_high_priority(self):
        return [do[0] for do in self.things if do[1] == self.maximum]