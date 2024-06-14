from datetime import datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

total = 0

for i in data:
    start_time = datetime.strptime(i[0], '%H:%M')
    end_time = datetime.strptime(i[1], '%H:%M')

    diff = end_time - timedelta(hours=start_time.hour, minutes=start_time.minute)

    total += diff.hour * 60 + diff.minute

print(total)