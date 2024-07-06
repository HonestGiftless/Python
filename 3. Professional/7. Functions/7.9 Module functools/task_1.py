# Two functions

# Вам доступна уже реализованная функция send_email(), которая принимает три аргумента в следующем порядке:
    # name — имя
    # email_address — адрес электронной почты
    # text — содержание письма
# Функция отправляет письмо пользователю с именем name на адрес email_address с содержанием text.

from functools import partial, update_wrapper

to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')

send_an_invitation = partial(send_email, text="Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....")