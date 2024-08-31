# ReversibleString
class ReversibleString:
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return self.string
    
    def __neg__(self):
        return ReversibleString(self.string[::-1])