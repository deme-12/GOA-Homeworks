# # while loop 

# # num = 0

# # while num < 10:
# #     print("helo")
# #     num = num + 1   #  num += 1  


# 1) ერთიდან 100 მდე დაბეჭდეთ ყველა რიცხვი while loop ის გამოყენებით

num = 1
while num <= 100:
    print(num)
    num += 1

#      2) ერთიდან 100 მდე დაბეჭდეთ ყველა ლუწი რიცხვი while loop ის გამოყენებით if ების გარეშე
num = 2
while num <= 100:
    print(num)
    num += 2

#      3) ერთიდან 100 მდე დაბეჭდეთ ყველა ლუწი რიცხვი while loop ის გამოყენებით if ების გამოყენებით
num = 2
while num <= 100:
    if num % 2 == 0:
        print(num)
        num += 2
#      4) ერთიდან 100 მდე დაბეჭდეთ ყველა რიცხვი თან გვერძე მიუწერეთ ლუწია თუ კენტი  while loop ის გამოყენებით

num = 0
while num <= 100:
    if num % 2 == 0:
        print(str(num) + " even")
    else:
        print(str(num) + " odd")
    num += 1  