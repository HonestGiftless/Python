# Класс Scales

class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, m):
        self.right += m

    def add_left(self, m):
        self.left += m

    def get_result(self):
        if self.right == self.left:
            return "Весы в равновесии"
        elif self.right > self.left:
            return "Правая чаша тяжелее"
        else:
            return "Левая чаша тяжелее"