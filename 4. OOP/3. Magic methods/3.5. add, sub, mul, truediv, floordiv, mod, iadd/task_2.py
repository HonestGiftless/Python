# Vector
class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, value):
        if isinstance(value, Vector):
            return Vector(self.x + value.x, self.y + value.y)
        return NotImplemented
    
    def __sub__(self, value):
        if isinstance(value, Vector):
            return Vector(self.x - value.x, self.y - value.y)
        return NotImplemented
    
    def __mul__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return Vector(self.x * value, self.y * value)
        return NotImplemented
    
    def __rmul__(self, value):
        return self.__mul__(value)
    
    def __truediv__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return Vector(self.x / value, self.y / value)
        return NotImplemented