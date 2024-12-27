def dont_give_me_five(start,end):
    result = 0
    for i in range(start, end + 1):
        if "5" not in str(i):
            result += 1
    return result

