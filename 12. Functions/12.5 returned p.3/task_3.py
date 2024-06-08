# Корни уравнения 🌶️🌶️

def solve(a, b, c):
    d = (b**2) - (4 * a * c)
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)

        if x1 > x2:
            return x2, x1
        else:
            return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)

        return x1, x2

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)