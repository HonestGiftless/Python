# Different types

import json

with open('data.json') as file, open('updated_data.json', 'w') as output:
    data = json.load(file)
    result = list()
    for i in data:
        if type(i) == str:
            i += '!'
        elif type(i) == int or type(i) == float:
            i += 1
        elif i == True or i == False:
            i = not i
        elif type(i) == list:
            i *= 2
        elif type(i) == dict:
            i["newkey"] = None
        elif i == None:
            continue
        result.append(i)

    json.dump(result, output, indent=3)