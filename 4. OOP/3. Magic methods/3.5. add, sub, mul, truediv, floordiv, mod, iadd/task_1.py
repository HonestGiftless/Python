# FoodInfo
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates) -> None:
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self) -> str:
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, value):
        if isinstance(value, FoodInfo):
            return FoodInfo(self.proteins + value.proteins, self.fats + value.fats, self.carbohydrates + value.carbohydrates)
        return NotImplemented
    
    def __mul__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return FoodInfo(self.proteins * value, self.fats * value, self.carbohydrates * value)
        return NotImplemented
    
    def __truediv__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return FoodInfo(self.proteins / value, self.fats / value, self.carbohydrates / value)
        return NotImplemented
    
    def __floordiv__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return FoodInfo(self.proteins // value, self.fats // value, self.carbohydrates // value)
        return NotImplemented