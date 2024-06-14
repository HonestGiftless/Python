# Timer

from datetime import datetime, timedelta

datetm = datetime.strptime(input(), '%H:%M:%S')
sec = int(input())

result = datetm + timedelta(seconds=sec)

print(result.time())