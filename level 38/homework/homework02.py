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