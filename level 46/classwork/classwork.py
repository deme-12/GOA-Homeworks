def str_sum(arr):
    result = ""
    minus = False
    
    for number in arr:
        if "-" in str(number):
            result += str(number).replace("-", "")
            minus = True
        else:
            result += str(number)
    
    if minus:
        return -int(result)
    else:
        return int(result)





def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []
    if not array1:
        return array2
    if not array2:
        return array1
    
    result = []
    total_sum = str_sum(array1) + str_sum(array2)
    
    if total_sum >= 0:
        for char in str(total_sum):
            result.append(int(char))
    else:
        for char in str(total_sum)[1:]:
            result.append(int(char))
        result[0] *= -1
    
    return result






def compute_sum(n):
    total_sum = 0
    
    for number in range(1, n + 1):
        str_number = str(number)
        if len(str_number) > 1:
            for char in str_number:
                total_sum += int(char)
        else:
            total_sum += number