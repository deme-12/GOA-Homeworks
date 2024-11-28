# 9) შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა. თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში, სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია

var1 = []
var2 = []

for i in range(5):
    fruits = input("enter favorite fruits ")
    if len(fruits) < 5:
        var1.append(fruits)
    else:
        var2.append(fruits)
print("var 1:", var1)
print("var 2:", var2)