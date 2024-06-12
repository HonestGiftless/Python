# Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
# и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    new_list = list()

    for word in ignore:
        if word in command:
            new_list.append(True)
    new_list.append(False)

    if any(new_list):
        return True
    else:
        return False