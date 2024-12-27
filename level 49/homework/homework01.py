def reverse_it(data):
    if isinstance(data, (str, int, float)):  
        return type(data)(str(data)[::-1])  
    return data  
