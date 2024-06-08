# Is Valid Triangle?

def is_valid_triangle(side1, side2, side3):
    if side1 < (side2 + side3) and side2 < (side1 + side3) and side3 < (side2 + side1):
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))