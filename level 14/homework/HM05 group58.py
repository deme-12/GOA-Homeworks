# 5) შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. საბოლოოდ დაპრინტეთ ეს სია(გამოიყენეთ for loop)

even_numbers = []

for i in range(1,101):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)