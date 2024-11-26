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

# ჯგუფი 58 საკლასო 
while True:
    print("go on")
    user_input = input("enter your question or exit to quit ")

    if user_input . lower() == "how are you":
        print("i am doing well thanks you")
    elif user_input == "whats the weather like?":
        print("its sunny and warm today")
    elif user_input == "give me bitcoin":
        print("sorry i cant give you bitcoin")
    elif user_input == "hack NASA":
        print("sorry i cant do that i am programer")
    elif user_input == "exit":
        print("goodbye!")
        break
    else:
        print()
    