# Трудности перевода

humans_count = int(input())
human_languages = dict()

for i in range(humans_count):
    languages = [i.lower() for i in input().split(", ")]
    human_languages[i] = languages

result_dict = dict()

for k, v in human_languages.items():
    for j in range(len(v)):
        if v[j] not in result_dict:
            result_dict[v[j]] = 1
        else:
            result_dict[v[j]] += 1

result_dict = dict(sorted(result_dict.items()))

result = []
for k, v in result_dict.items():
    if v == humans_count:
        result.append(k)

if len(result) > 0:
    print(*result, sep=', ')
else:
    print("Сериал снять не удастся")