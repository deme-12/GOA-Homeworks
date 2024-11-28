# 2) შექმენით ხილების სია, სადაც გექნებათ მინიმუმ 3 ელემენტი. მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი, თუ სიის ბოლო ელემენტის ინდექსი არის ლუწი ჩაამატეთ შემოტანილი ხილი სიაში, სხვა შემთხვევაში არ ჩაამატოთ 

fruits = ["banana","grapes","kiwi"]
fruits_favorite = input("enter favorite fruits ")
if (len(fruits)-1) % 2 == 0:
    fruits.append(fruits_favorite)
    print(fruits)

