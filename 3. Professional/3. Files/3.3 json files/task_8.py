# Combining objects

import json

with open('data1.json') as data1, open('data2.json') as data2, open('data_merge.json', 'w') as output:
    data_from_first = json.load(data1)
    data_from_sec = json.load(data2)

    merged_dictionary = {**data_from_first, **data_from_sec}
    json_data = json.dump(merged_dictionary, output, indent=3, sort_keys=True)