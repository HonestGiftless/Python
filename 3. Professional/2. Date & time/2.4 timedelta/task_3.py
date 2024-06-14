# Previous & next date

from datetime import datetime, timedelta, date

text = input()

user_date = date(day=int(text.split('.')[0]), month=int(text.split('.')[1]), year=int(text.split('.')[2]))

print((user_date - timedelta(days=1)).strftime('%d.%m.%Y'))
print((user_date + timedelta(days=1)).strftime('%d.%m.%Y'))