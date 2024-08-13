# Annuity

def annual_return(start: int, percent: int, years: int):
    result = []
    for _ in range(years):
        summ = start * ((100 + percent) / 100)
        result.append(summ)
        start = summ

    result = iter(result)
    yield from result