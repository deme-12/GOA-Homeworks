def high_and_low(numbers):
    numbers = numbers.split(" ")
    min_number = int(numbers[0])
    max_number = int(numbers[0])
    for num in numbers:
        if min_number > int(num):
            min_number = int(num)
        elif max_number < int(num):
            max_number = int(num)