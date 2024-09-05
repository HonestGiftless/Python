# DateFormatter
from datetime import date

class DateFormatter:
    def __init__(self, country_code) -> None:
        self.country_code = country_code

    def __call__(self, d):
        dates = {'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y',}

        return str(date.strftime(d, dates[self.country_code]))