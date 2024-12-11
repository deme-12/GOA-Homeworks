def backwards_prime(start, stop):
    def is_prime(n):
        for i in range(2,int(n ** 0.5) +1):
            if n % i == 0:
                return False
        return True
    
    new_list = []
    for i in range(start,stop + 1):
        if is_prime(i):
            reversed_numb = int(str(i)[::-1])
            if is_prime(reversed_numb) and i >= 10 and i != reversed_numb:
                new_list.append(i)        
    return new_list