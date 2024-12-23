def reverse_bits(n):
    binary = bin(n)[2:]
    str_bin = binary[::-1]

    result = 0
    for i in range(len(str_bin)):
        result += int(str_bin[i]) * (2 ** (len(str_bin) - (i +1)))
    return result





