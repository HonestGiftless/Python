# SuperString
class SuperString:
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return self.string
    
    def __add__(self, value):
        if isinstance(value, SuperString):
            return SuperString(self.string + value.string)
        return NotImplemented
    
    def __mul__(self, value):
        if isinstance(value, int):
            return SuperString(self.string * value)
        return NotImplemented
    
    def __rmul__(self, value):
        return self.__mul__(value)
    
    def __truediv__(self, value):
        if isinstance(value, int):
            m = len(self.string) // value
            return SuperString(self.string[:m])
        return NotImplemented
        
    def __lshift__(self, value):
        if isinstance(value, int):
            if value >= len(self.string):
                return SuperString('')
            else:
                if value > 0:
                    return SuperString(self.string[:-value])
                else:
                    return SuperString(self.string)
        return NotImplemented
    
    def __rshift__(self, value):
        if isinstance(value, int):
            if value >= len(self.string):
                return SuperString('')
            else:
                if value > 0:
                    return SuperString(self.string[value:])
                else:
                    return SuperString(self.string)
        return NotImplemented