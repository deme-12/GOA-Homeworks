def high_and_low(numbers):
    num_list =list(map(int,numbers.split()))
    highest = max(num_list)
    lowest = min(num_list)
    
    return f"{highest} {lowest}"