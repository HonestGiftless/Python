#  is_available_date() 🌶️

from datetime import datetime, timedelta

def is_available_date(booked_dates, date_for_booking):
    cleanest = True

    book_dates = list()
    needed_dates = list()

    if "-" in date_for_booking:
        start_for_date = datetime.strptime(date_for_booking.split("-")[0], '%d.%m.%Y')
        end_for_date = datetime.strptime(date_for_booking.split("-")[1], '%d.%m.%Y')
        while start_for_date  <= end_for_date:
            needed_dates.append(start_for_date)
            start_for_date += timedelta(days=1)
    else:
        needed_dates.append(datetime.strptime(date_for_booking, '%d.%m.%Y'))

    for date in booked_dates:
        if "-" in date:
            start_date = datetime.strptime(date.split("-")[0], '%d.%m.%Y')
            end_date = datetime.strptime(date.split("-")[1], '%d.%m.%Y')
            while start_date <= end_date:
                book_dates.append(start_date)
                start_date += timedelta(days=1)
        else:
            book_dates.append(datetime.strptime(date, '%d.%m.%Y'))
    
    for i in needed_dates:
        if i in book_dates:
            cleanest = False
            break

    if cleanest:
        return True
    else:
        return False