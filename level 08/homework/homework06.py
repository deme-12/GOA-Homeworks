#6 შეამოწმე მომხმარებლის შემოტანილი რიცხვი თუ არის 5-ის ან 10-ის ჯერადი.

num = int(input("enter number: "))
if num % 5 == 0 or num % 10 == 0:
    print("True")
else:
    print("False")
