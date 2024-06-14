# Реп по матеше

from datetime import datetime, timedelta

start_time = datetime.strptime(input(), '%H:%M')
end_time = datetime.strptime(input(), '%H:%M')

end_of_lesson = start_time

while end_of_lesson != end_time:
    if (start_time + timedelta(minutes=45) <= end_time):
        end_of_lesson = start_time + timedelta(minutes=45)
        print(datetime.strftime(start_time, '%H:%M'), '-', datetime.strftime(end_of_lesson, '%H:%M'))
        start_time = end_of_lesson + timedelta(minutes=10)
    else:
        break