# 6) შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. შემდეგ გადაუარეთ for loop-ით და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი. საბოლოოდ დაპრინტეთ მიღებული სია

numb = []

for num in range(1,51):
    numb.append(num)
for num in numb:
    if num % 2 != 0:
        numb.remove(num)
print(numb)