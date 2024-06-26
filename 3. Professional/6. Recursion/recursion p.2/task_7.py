# recursive_sum()

def recursive_sum(a, b):
    if a == 0:
        if b == 0:
            return 0
        else:
            return 1 + recursive_sum(a, b - 1)
    else:
        if b == 0:
            return 1 + recursive_sum(a - 1, b)
        else:
            return 1 + recursive_sum(a, b - 1)