# Number of files

from zipfile import ZipFile

counter = 0

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for i in info:
        if not i.is_dir():
            counter += 1

print(counter)