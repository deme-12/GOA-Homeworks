#12 შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.
num1 = int(input("enter number: "))
num2 = int(input("enter second number: "))   

if num1 > num2 and num1 % 10 == 0:
    print("num1 greater than num2 and is divisible by 10") 
elif num2 > num1 and num2 % 10 == 0:
    print("num2 greater than num1 and is divisible by 10") 


