# Archive structure 🌶️ 🌶️

from zipfile import ZipFile

def convert_bytes(size):
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile("desktop.zip") as zip_file:
    data = zip_file.infolist()
    
    for i in data:
        if "/" in i.filename:
            path = [j for j in i.filename.split("/") if j != ""]
        else:
            path = [i.filename]

        if "." not in path[-1]:
            print("  " * (len(path) - 1), path[-1], sep="")
        else:
            print("  " * (len(path) - 1), path[-1], " ", convert_bytes(i.file_size), sep="")
