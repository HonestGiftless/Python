# Formatted output

from zipfile import ZipFile
from datetime import datetime

rst = list()

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    files = sorted([i for i in info if not i.is_dir()], key=lambda item: item.filename.split("/")[-1])

    for file in files:
        print(file.filename.split("/")[-1])
        print(f"  Дата модификации файла: {datetime(*file.date_time)}")
        print(f"  Объем исходного файла: {file.file_size} байт(а)")
        print(f"  Объем сжатого файла: {file.compress_size} байт(а)")
        print()