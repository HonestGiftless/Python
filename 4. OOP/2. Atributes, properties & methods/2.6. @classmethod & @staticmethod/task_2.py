# Rectangle

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)