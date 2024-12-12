
def reverse_bits(n):
    binary = bin(n)[2:]
    str_bin = binary[::-1]

    result = 0
    for i in range(len(str_bin)):
        result += int(str_bin[i]) * (2 ** (len(str_bin) - (i +1)))
    return result



def calculator(txt):
    str_list = txt.split()

    s1 = len(str_list[0])
    s2 = len(str_list[2])

    if str_list[1] == "+": return (s1 + s2) * "."
    elif str_list[1] == "-": return (s1 - s2) * "."
    elif str_list[1] == "*": return (s1 * s2) * "."

    return (s1 // s2) * "."




def move_zeros(lst):
    result = []
    zeros = []
    for num in lst:
        if num != 0: result.append(num)
        else: zeros.append(num)
    return result + zeros


