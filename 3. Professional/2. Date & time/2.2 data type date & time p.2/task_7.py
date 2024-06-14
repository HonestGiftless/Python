# print_good_dates()

from datetime import date

def print_good_dates(dates):
    dates = sorted(dates)
    for data in dates:
        if data.strftime('%Y') == "1992":
            if int(data.strftime('%m')) + int(data.strftime('%d')) == 29:
                print(data.strftime('%B %d, %Y'))