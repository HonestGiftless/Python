# I didn't have time again

from datetime import datetime, timedelta

working_hours = {
    0: ('09:00', '21:00'),
    1: ('09:00', '21:00'),
    2: ('09:00', '21:00'),
    3: ('09:00', '21:00'),
    4: ('09:00', '21:00'),
    5: ('10:00', '18:00'),
    6: ('10:00', '18:00')
}

user_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
user_time = user_date.time()

if user_time < datetime.strptime(working_hours[user_date.weekday()][0], '%H:%M').time():
    print("Магазин не работает")
else:
    if user_time > datetime.strptime(working_hours[user_date.weekday()][1], '%H:%M').time():
        print("Магазин не работает")
    else:
        result = datetime.strptime(working_hours[user_date.weekday()][1], '%H:%M') - timedelta(hours=user_time.hour, minutes=user_time.minute)
        if result.hour * 60 + result.minute > 0:
            print(result.hour * 60 + result.minute)
        else:
            print("Магазин не работает")