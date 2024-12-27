def nth_char(words):
    result = ""
    index = 0
    for i in words:
        result += i[index]
        index += 1
    return result


def greet(name):
    return None if not name else "hello " + name + "!"


def calculate(s):
    
    string1 = " ".join(s.replace("plus", "+").replace("minus", "-").split("+"))
    str2 = string1[0]
    for i in string1[1:]:
        if i == "-":
            str2 += " -"
        else:
            str2 += i
    result = 0
    
    for i in str2.split():
        result += int(i)
    return str(result)