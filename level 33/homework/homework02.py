def reverse_number(n):
    if n < 0:
        return -int(str(n * -1)[::-1])
    else:
        return int(str(n)[::-1])