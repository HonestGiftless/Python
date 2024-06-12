# Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране в формате:

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

items = list(zip(capitals, countries, population))

for item in items:
    print(f'{item[0]} is the capital of {item[1]}, population equal {item[2]} people.')