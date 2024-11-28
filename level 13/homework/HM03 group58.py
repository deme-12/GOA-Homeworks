# 3) შექმენით სია შემდგარი სახელებისგან. მომხარებელს შემოატანინეთ მისი სახელი, თუ მისი სახელი იქნება 5 სიმბოლოს ტოლი ან მეტი. ჩაამატეთ სიაში, სხვა შემთხვევაში დაუბეჭდეთ "Name is too short"

names = ["janine","david","tomas","michael","sophia"]
name = input("enter your name")
if len(name) >= 5:
    names.append(name)
    print(names)
else:
    print("Name is too short")
