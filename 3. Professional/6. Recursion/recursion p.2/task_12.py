# Without cycles

def without_cycles(number, count=5):
    if number > 0:
        print(number)
        without_cycles(number - count)
    print(number)
    
without_cycles(int(input()))