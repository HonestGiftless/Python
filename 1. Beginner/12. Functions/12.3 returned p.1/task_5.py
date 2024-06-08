# Найти всех

def find_all(target, symbol):
    l = []
    for i in range(len(target)):
        if target[i] == symbol:
            l.append(i)
    return l

s = input()
char = input()

print(find_all(s, char))