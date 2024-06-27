# Unusual sorting 🌶️

string = input()

result = sorted([i for i in string if i.islower()]) + sorted([i for i in string if i.isupper()]) + sorted([i for i in string if i.isdigit() and int(i) % 2 != 0]) + sorted([i for i in string if i.isdigit() and int(i) % 2 == 0])

print("".join(result))