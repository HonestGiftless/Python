import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    text = csv.reader(csv_file, delimiter=';')
    
    for row in text:
        print(row)