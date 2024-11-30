# classwork N1

def positive_sum(arr):
    sum = 0
    for num in arr:
        if num >0:
            sum += num
    return sum

# classwork N2

def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num ** 2
    return sum

#  classwork N3

def sum_array(a):
    sum = 0
    for num in a:
        sum += num
    return sum

# classwork N4

def find_average(numbers):
    if len(numbers) == 0:
        return 0    
    sum = 0 
    for num in numbers:
        sum += num
    return sum / len(numbers)

# classwork N5

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count = 0
    sum = 0
    for num in arr:
        if num > 0:
            count += 1
        else:
            sum += num         
    return [count,sum]

