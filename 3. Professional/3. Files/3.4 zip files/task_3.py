# The best indicator

from zipfile import ZipFile

rst = dict()

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()

    maximal = max(info, key=lambda x: 100 - ((x.compress_size / x.file_size) * 100) if not x.is_dir() else 0)
    
    print(maximal.filename.split("/")[-1])