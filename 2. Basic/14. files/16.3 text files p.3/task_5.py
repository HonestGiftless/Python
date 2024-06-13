# Загадка от Жака Фреско 🌶️

all_colors = list()
all_goat = list()

with open("goats.txt", "r", encoding="utf-8") as file:
    for i in file:
        if i != "GOATS\n":
            all_colors.append(i)
        else:
            break
    for i in file:
        all_goat.append(i.strip('\n'))

all_colors = [i.strip('\n') for i in all_colors[1:]]
all_goat_dict = {k: all_goat.count(k) for k in all_goat}

all_count = sum(list(all_goat_dict.values()))

with open("answer.txt", 'w', encoding='utf-8') as output:
    for k, v in all_goat_dict.items():
        if v > all_count / 100 * 7:
            print(k, file=output)