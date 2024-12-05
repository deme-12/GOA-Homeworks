# 2) შექმენით ფუნქცია manual_len, რომელსაც გადაეცემა სთრინგი ან სია, ხოლო ფუნქციამ უნდა დააბრუნოს გადმოცემული სთრინგის/სიის სიგრძე(არ გამოიყენოთ len-ი)

def manual_list(lst):
    count = 0
    for char in lst:
        count += 1
    return count

print(manual_list("Hello World"))

print(manual_list([1,2,3,4,5]))
