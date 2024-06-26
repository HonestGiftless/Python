# linear()

def linear(nested_list):
    result = list()
    for i in nested_list:
        if type(i) == int:
            result.append(i)
        else:
            result.extend(linear(i))
    
    return result