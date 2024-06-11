# Опасный вирус 😈

result = []

operations = {'write': 'W',
              'read': 'R',
              'execute': 'X'}

files_count = int(input())
files = dict()

for i in range(files_count):
    file = input().split()
    if len(file) == 2:
        files[file[0]] = file[1]
    else:
        files[file[0]] = " ".join(file[1:]).split()

user_choice_count = int(input())

for i in range(user_choice_count):
    user_action = input().split()

    if operations[user_action[0]] in files[user_action[1]]:
        result.append("OK")
    else:
        result.append("Access denied")

print(*result, sep='\n')