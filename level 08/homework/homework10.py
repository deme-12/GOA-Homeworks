#10 დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი ან 3-ის ჯერადი. 
num = int(input("enter number: "))
if num % 2 == 0 or num % 3 == 0:
    print("True")
else:
    print("False")
