from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = today - birthday

print(abs(days.days))