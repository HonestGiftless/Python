# QuadraticPolynomial

class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_iterable(cls, iterable):
        iterable = list(iterable)
        return cls(iterable[0], iterable[1], iterable[2])
    
    @classmethod
    def from_str(cls, string):
        string = string.split()
        for i in range(len(string)):
            if '.' in string[i]:
                string[i] = float(string[i])
            else:
                string[i] = int(string[i])
        return cls(string[0], string[1], string[2])