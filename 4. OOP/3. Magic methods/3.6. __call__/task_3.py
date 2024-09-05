# Dice
import random

class Dice:
    def __init__(self, sides) -> None:
        self.sides = sides

    def __call__(self):
        return random.choice([i for i in range(1, self.sides + 1)])