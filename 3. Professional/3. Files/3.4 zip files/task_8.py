# extract_this()

from zipfile import ZipFile
import os.path

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if len(args) > 0:
            for i in args:
                zip_file.extract(i)
        else:
            zip_file.extractall()