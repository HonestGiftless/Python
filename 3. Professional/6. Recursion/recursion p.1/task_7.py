# Hourglass

def watch(number, count):
    if number < 4:
        
        print(f"{str(number) * count}".center(16))
        watch(number + 1, count - 4)
    print(f"{str(number) * count}".center(16))

watch(1, 16)