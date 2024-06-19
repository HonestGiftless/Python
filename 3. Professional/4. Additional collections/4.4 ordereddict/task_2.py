from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()
boolean_values = [False if i % 2 == 0 else True for i in range(len(data))]

for rule in boolean_values:
    key, value = data.popitem(last=rule)
    new_data[key] = value

print(new_data)