# Звездный треугольник

def draw_triangle(fill, base):
    average = base // 2 + 1

    for i in range(1, average + 1):
        if i < average:
            print(i * fill)
        else:
            for j in range(average, 0, -1):
                print(j * fill)

fill = input()
base = int(input())

draw_triangle(fill, base)