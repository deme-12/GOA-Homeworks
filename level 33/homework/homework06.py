def kebabize(st):
    result = ""
    for char in st:
        if char.isalpha():
            if char.isupper():
                result += "-" + char.lower()
            else:
                result += char
    if len(result) > 0 and result[0] == "-":
        return result[1:]
    return result        