# Calculator
class Calculator:
    def __call__(self, a, b, operation):
        if b != 0:
            return eval(f"{a} {operation} {b}")
        else:
            if operation != '/':
                return eval(f"{a} {operation} {b}")
            raise ValueError("Деление на ноль невозможно")