# Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.

is_num = lambda num: num.replace('.', '', 1).replace('-', '', 1).isdigit() if '-' == num[0] or '-' not in num else False