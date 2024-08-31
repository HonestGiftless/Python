# Vector
import math

class Vector:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __pos__(self):
        return self.__class__(self.x, self.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __abs__(self):
        return math.sqrt((self.x**2) + (self.y**2))