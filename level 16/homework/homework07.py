#      7) დაბეჭდეთ 100 დან 200 მდე ყველა რიცხვი გვერძე კი მიუწერეთ ლუწია თუ კენტი გამოიყენეთ while loop და if else

num = 100
while num <= 200:
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
    num += 1
