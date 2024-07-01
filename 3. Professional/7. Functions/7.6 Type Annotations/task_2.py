# top_grade()

def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    '''Функция принимает словарь с ключами-строками, а значениями строками или списком чисел
    Возвращает словарь с именем (строка) и максимальной оценкой ученика (строка или число)'''
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}