def compute_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += sum(int(digit) for digit in str(i)) 
    return result
print(compute_sum(5))