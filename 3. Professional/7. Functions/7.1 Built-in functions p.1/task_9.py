names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

result = sorted([(i[0], i[2]-i[1]) for i in zip(names, budgets, box_offices)], key=lambda item: item[0])

for i in result:
    print(f"{i[0]}: {i[1]}$")