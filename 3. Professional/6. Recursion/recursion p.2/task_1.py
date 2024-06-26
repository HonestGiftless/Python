# Number of digits

def num_count(num):
    if num == 0:
        return 0
    else:
        return 1 + num_count(num // 10)
    
print(num_count(int(input())))