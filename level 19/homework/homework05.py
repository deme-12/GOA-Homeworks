# 5) შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით, გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობა

numb = [10,12,3,13,15,16,34,56,66,63]

even_count = 0
odd_count = 0

for num in numb:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count)
print(odd_count)