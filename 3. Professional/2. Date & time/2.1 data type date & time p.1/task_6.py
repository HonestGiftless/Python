# get_date_range()

def get_date_range(start, end):
    st = start.toordinal()
    ed = end.toordinal()
    res_lst = list()

    if st < ed:
        for i in range(st, ed + 1):
            res_lst.append(date.fromordinal(i))
    elif st == ed:
        res_lst.append(start)
    else:
        res_lst = list()

    return res_lst