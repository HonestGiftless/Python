# Статистика по файлу

def char_symbols(object, frm, to, frm2, to2): # Функция получения латинских букв
    for i in range(frm, to):
        object.append(chr(i))
    for i in range(frm2, to2):
        object.append(chr(i))

with open('file.txt', 'r', encoding='utf-8') as file:
    lst = file.readlines() # Список из строк файла
    lines_counter = len(lst) # Длина списка => количество строк
    words_counter, symbols_counter = 0, 0 # Определения счетчиков
    chars_list, strips_list = list(), list() # Список для символов и список отсортированных без \n чисел
    sorted_lst = list()

    char_symbols(chars_list, 65, 91, 76, 123)

    for i in lst:
        strips_list.append(i.strip('\n'))
    
    for i in strips_list:
        words_counter += len(i.split())

    for i in strips_list:
        res_str = ''
        for j in i:
            if j in chars_list:
                res_str += j
        sorted_lst.append(res_str)
    
    for i in sorted_lst:
        symbols_counter += len(i)

    print(f'Input file contains:\n{symbols_counter} letters\n{words_counter} words\n{lines_counter} lines')