#15 დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ერთდროულად 50-ზე ნაკლები და 10-ის ჯერადი.
num = int(input("enter number: "))
if num < 50 and num % 10 == 0:
    print("True")
else:
    print("False")