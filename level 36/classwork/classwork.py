def vaporcode(s):
    return "  ".join(s.upper().replace(" ",""))


def capitals(word):
    nums = []
    for i in range(len(word)):
        if word[i].isupper():
                nums.append(i)
    return nums


def nb_dig(n, d):
    count = 0
    for i in range(0, n + 1):
        squared_num = i ** 2
        count += str(squared_num).count(str(d))
    return count



def symbols(string):
    unique_symbols = []
    for char in string:
        if char not in unique_symbols:
            unique_symbols.append(char)
    return len(unique_symbols)
print(symbols("goaa aaccademmy"))


# kababize
def kababize(st):
    numbers_str = "0123456789"
    result = ""
    for i in st:
        if i.isupper():
            result += "-" + i.lower()
            result += i
    if result[0] == "-" and result != "":
        return result[1:]
    return result 


# manual range

def manual_range(start,end,step):
    i = start
    while i < end:
        print(i)
        i += step
manual_range(10,200,10)