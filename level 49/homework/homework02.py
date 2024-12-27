def find_missing_numbers(arr):
    missing = [] 
    if not arr:
        return []
    for num in range(arr[0], arr[-1] + 1): 
        if num not in arr: 
            missing.append(num)  
    return missing 