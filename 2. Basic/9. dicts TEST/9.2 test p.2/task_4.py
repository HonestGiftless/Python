# Строка запроса

def build_query_string(dct):
    query = []
    for key, value in dct.items():
        query_string = str(key) + '=' + str(value)
        query.append(query_string)
    query = sorted(query)
    return '&'.join(query)