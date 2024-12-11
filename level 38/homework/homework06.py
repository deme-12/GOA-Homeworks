def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    def is_eurica(n):
        sum = 0
        position = 1
        for i in str(n):
            sum += int(i) ** position
            position += 1
        return sum == n
    
    new_list = []
    for i in range(a,b + 1):
        if is_eurica(i):
            new_list.append(i)
    return new_list