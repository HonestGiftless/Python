# FAKE NEWS 🌶️

from datetime import datetime, timedelta

def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f"{amount} {declensions[0]}"
    elif 2 <= amount % 10 <= 4 and not 12 <= amount % 100 <= 14:
        return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[2]}"
    
def hours(td):
    return td.seconds // 3600

def minutes(td):
    return (td.seconds // 60) % 60

drop_time = datetime(year=2022, month=11, day=8, hour=12)

user_time = input().split()
current_time = datetime.strptime(user_time[0], '%d.%m.%Y') + timedelta(hours=int(user_time[1].split(':')[0]), minutes=int(user_time[1].split(':')[1]))

result = drop_time - current_time

if current_time < drop_time:
    if result.days > 0:
        if hours(result) > 0:
            print("До выхода курса осталось:", choose_plural(result.days, ["день", "дня", "дней"]), "и", choose_plural(hours(result), ["час", "часа", "часов"]))
        else:
            print("До выхода курса осталось:", choose_plural(result.days, ["день", "дня", "дней"]))
    elif result.days <= 0:
        if hours(result) > 0:
            if minutes(result) > 0:
                print("До выхода курса осталось:", choose_plural(hours(result), ["час", "часа", "часов"]), "и", choose_plural(minutes(result), ["минуты", "минута", "минут"]))
            else:
                print("До выхода курса осталось:", choose_plural(hours(result), ["час", "часа", "часов"]))
        else:
            print("До выхода курса осталось:", choose_plural(minutes(result), ["минута", "минуты", "минут"]))

else:
    print("Курс уже вышел!")