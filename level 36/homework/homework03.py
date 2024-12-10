# Bit Counting

def count_bits(n):
    binary = "0"
    while n != 0:
        binary += str(n % 2)
        n = n // 2
    return binary.count("1")
