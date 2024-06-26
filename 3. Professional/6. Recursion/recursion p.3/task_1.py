# recursive_sum()

def recursive_sum(nested_list):    
    if len(nested_list) == 0:
        return 0
    else:
        result = 0
        for i in nested_list:
            if type(i) == int:
                result += i
            else:
                result += recursive_sum(i)
        return result