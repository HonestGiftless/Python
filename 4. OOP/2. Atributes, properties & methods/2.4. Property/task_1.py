# Rectangle

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def perimeter(self):
        return self.length * 2 + self.width * 2
    
    def area(self):
        return self.length * self.width
    
    perimeter = property(perimeter)
    area = property(area)