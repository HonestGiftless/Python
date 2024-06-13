# Goooood students

with open('grades.txt', 'r', encoding='utf-8') as file:
    result = []

    for i in file.readlines():
        grades_list = i.split()
        if int(grades_list[1]) >= 65 and int(grades_list[2]) >= 65 and int(grades_list[3]) >= 65:
            result.append(grades_list)
    
    print(len(result))