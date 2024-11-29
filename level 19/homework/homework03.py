# 3) შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი

numb = [12,10,4,15,23,45,65,45,76,97]

min_num = numb[1]
max_num =numb[3]

for num in numb:
    if  min_num > num:
        min_num = num
    elif max_num < num:
        max_num = num
print(min_num)
print(max_num)


# min_num = min(numb) #ს ფუნქცია პოულობს სიის ყველაზე პატარა რიცხვს.
# max_num = max(numb) #ეს ფუნქცია პოულობს სიის ყველაზე დიდ რიცხვს. 
# print(min_num + max_num)

