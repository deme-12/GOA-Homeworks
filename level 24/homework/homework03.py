def accum(st):
    result = []
    counter = 1
    for char in st:
        result.append((char * counter).capitalize())
        counter += 1
    return "-".join(result)