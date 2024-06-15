# Chess was better 🌶️

from zipfile import ZipFile
import json

def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False
    
result = list()
    
with ZipFile("data.zip") as zip_file:
    files = [i for i in zip_file.infolist() if not i.is_dir()]
    
    for file in files:
        if file.filename.split("/")[-1].split(".")[-1] == "json":
            with zip_file.open(file) as json_file:
                try:
                    json_data = json_file.read().decode("utf-8")
                except:
                    continue

                if is_correct_json(json_data):
                    json_data = json.loads(json_data)
                    if json_data["team"].lower() == "arsenal":
                        name = json_data["first_name"] + ' ' + json_data["last_name"]
                        result.append(name)

result = sorted(result, key=lambda item: (item.split()[0], item.split()[1]))
print(*result, sep='\n')