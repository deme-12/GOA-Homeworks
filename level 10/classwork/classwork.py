# 1 ) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ ეს რიცხვი არის თუ არა სამის ჯერადი

num = int(input("enter number"))
if num % 3 == 0:
    print ("true")
else:
    print("false")


# 2) შეამოწმე არის თუ არა რიცხვი დადებითი 

num1 = int(input("enter number"))

if num1 > 0:
    print("positive")
elif num1 == 0:
    print("ypur number is 0")
else:
    print("negative")


product = "ბორჯომი"

if product == "ნაბეღლავი":
    print("ვიყიდოთ ნაბეღლავი")
elif product == "ბორჯომი":
    print("ვიყიდოთ ორჯომი")
