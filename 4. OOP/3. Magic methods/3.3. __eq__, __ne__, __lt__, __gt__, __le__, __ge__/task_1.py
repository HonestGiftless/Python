# Vector
class Vector:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, value) -> bool:
        if isinstance(value, Vector):
            return self.x == value.x and self.y == value.y
        elif isinstance(value, tuple) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]
        return NotImplemented