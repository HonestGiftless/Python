# Вершина параболы

def takeResult(a, b, c):
    x = -(b / (2 * a))
    y = (4 * a * c - b**2) / (4 * a)
    return x, y

a, b, c = int(input()), int(input()), int(input())

print(takeResult(a,b,c))