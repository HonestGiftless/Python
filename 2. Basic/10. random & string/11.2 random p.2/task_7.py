# Тайный друг 🌶️

import random

count = int(input())

friends = [input() for i in range(count)]
friends_dict = {i: '' for i in friends}
is_friend = {i: False for i in friends}

while not all(list(friends_dict.values())):
    for k in friends_dict.keys():
        choice = random.choice(friends)

        while is_friend[choice] or choice == k:
            choice = random.choice(friends)

        friends_dict[k] = choice
        is_friend[choice] = True

for key, value in friends_dict.items():
    print(f"{key} - {value}")