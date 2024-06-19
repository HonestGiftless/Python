from collections import Counter

def minimal():
    result = list()

    for k, v in data.items():
        if v == data.most_common()[-1][1]:
            result.append(tuple([k, v]))
    
    return result

def maximal():
    result = list()

    for k, v in data.items():
        if v == data.most_common()[0][1]:
            result.append(tuple([k, v]))
    
    return result

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values = minimal
data.max_values = maximal