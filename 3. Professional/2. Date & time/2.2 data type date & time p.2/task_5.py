# Two dates

from datetime import date, time

first_date = date.fromisoformat(input())
second_date = date.fromisoformat(input())

lst = [first_date, second_date]
early_date = min(lst)

print(early_date.strftime('%d-%m (%Y)'))