def divisors(n):
    divisors = 0
    for i in range(1,n+ 1):
        if n % i == 0:
            divisors += 1
    return divisors + 1


# N1 38 level
def sum_cubes(n):
    sum = 0
    for i in range(1,n + 1):
        sum += i ** 3
    return sum


# N2
def disarium_number(number):
    number = str(number)
    sum = 0
    i = 1
    for digit in number:
        sum += int(digit) ** i
        i += 1
    if int(number) == sum:
        return "Disarium !!"
    else:
        return "Not !!"



# N3

def most_frequent_item_count(collection):
    if collection == []:
        return 0
    return max([collection.count(i) for i in collection])


# N4

def in_asc_order(arr):
    return arr == sorted(arr)



# https://www.codewars.com/kata/56b7f2f3f18876033f000307

# https://www.codewars.com/kata/5aba780a6a176b029800041c

# 6 kyu
# https://www.codewars.com/kata/5626b561280a42ecc50000d1