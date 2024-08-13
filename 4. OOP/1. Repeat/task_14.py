# pluck

def pluck(data: dict, path: str, default=None):
    path = path.split('.')
    
    if len(path) == 1:
        if path[0] in data:
            return data[path[0]]
        
        for v in data.values():
            if type(v) == dict:
                value = pluck(v, path[0], default=default)
                if value is None:
                    return default
    else:
        for i in path:
            data = data.get(i, default)
        
        if data:
            return data
        else:
            return default