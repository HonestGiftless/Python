from math import sqrt

class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        d = (self.b**2) - (4 * self.a * self.c)

        if d == 0:
            if ((self.b)/(2*self.a)) != 0:
                return -((self.b)/(2*self.a))
            else:
                return ((self.b)/(2*self.a))
        elif d > 0:
            return ((-self.b)-sqrt(d))/(2*self.a)
        else:
            return None

    @property
    def x2(self):
        d = (self.b**2) - (4 * self.a * self.c)

        if d == 0:
            if ((self.b)/(2*self.a)) != 0:
                return -((self.b)/(2*self.a))
            else:
                return ((self.b)/(2*self.a))
        elif d > 0:
            return ((-self.b)+sqrt(d))/(2*self.a)
        else:
            return None
        
    @property
    def view(self):
        if self.b >= 0 and self.c >= 0:
            return f"{self.a}x^2 + {self.b}x + {self.c}"
        elif self.b >= 0 and self.c < 0:
            return f"{self.a}x^2 + {self.b}x - {abs(self.c)}"
        elif self.b < 0 and self.c >= 0:
            return f"{self.a}x^2 - {abs(self.b)}x + {self.c}"
        else:
            return f"{self.a}x^2 - {abs(self.b)}x - {abs(self.c)}"

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, data):
        self.a, self.b, self.c = data