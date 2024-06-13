# Функция likes()

def likes(names):
    if len(names) == 0:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        res_txt = ''
        for i in range(len(names)):
            if i == 0:
                res_txt += names[i] + ', '
            elif i == 1:
                res_txt += names[i] + ' и '
            else:
                if str(len(names) - 2) + ' других оценили данную запись' not in res_txt:
                    res_txt += str(len(names) - 2) + ' других оценили данную запись'

        return res_txt