#14 მომხმარებლის შემოტანილი რიცხვი შეამოწმე, არის თუ არა  20-ის ჯერადი და დადებითი.
num = int(input("enter number: "))
if num % 20 == 0 and num > 0:
    print(True)
else:
    print("False")