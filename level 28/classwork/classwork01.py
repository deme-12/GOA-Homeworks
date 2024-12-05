def high_and_low(numbers):
    splited_numbers = []
    string = ""

    for i in numbers + " ":
        if i == " ":
            splited_numbers.append(int(string))
            string = ""
        else:
            string += i
    return splited_numbers
print(high_and_low("1 2 3 4 5 6 7"))