# File size

from zipfile import ZipFile

files_size, compressed_size = 0, 0

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    for i in info:
        files_size += i.file_size
        compressed_size += i.compress_size

print(f"Объем исходных файлов: {files_size} байт(а)")
print(f"Объем сжатых файлов: {compressed_size} байт(а)")