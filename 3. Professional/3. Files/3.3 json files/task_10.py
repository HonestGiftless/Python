# Я исповедую Python, а ты?

import json

with open('countries.json') as file, open('religion.json', 'w') as output:
    result = list()
    rst_dict = dict()
    data = json.load(file)
    for i in data:
        if i['religion'] not in rst_dict.keys():
            rst_dict[i['religion']] = [i['country']]
        else:
            rst_dict[i['religion']] += [i['country']]
    
    for k, v in rst_dict.items():
        rst_dict[k] = sorted(v)

    json.dump(rst_dict, output, indent=3)