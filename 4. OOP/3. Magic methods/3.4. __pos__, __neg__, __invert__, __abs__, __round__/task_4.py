# ColoredPoint
class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)) -> None:
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)

    def __neg__(self):
        return self.__class__(self.x * -1, self.y * -1, self.color)
    
    def __invert__(self):
        return self.__class__(self.y, self.x, (abs(self.color[0] - 255), abs(self.color[1] - 255), abs(self.color[2] - 255)))