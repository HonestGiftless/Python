# Total seconds

from datetime import datetime, timedelta, time

text = input().split(':')
result = timedelta(hours=int(text[0]), minutes=int(text[1]), seconds=int(text[2]))

print(int(result.total_seconds()))