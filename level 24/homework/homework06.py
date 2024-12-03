def find_smallest_int(arr):
    min_numbers = arr[0]
    for num in arr:
        if min_numbers > num:
            min_numbers = num
    return min_numbers