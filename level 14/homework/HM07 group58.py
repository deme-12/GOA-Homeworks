# 7) შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი, while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია


fruits = ["grape","banana","kiwi","orange","pear","apple","melon","strawberies","granat","cherry"]

while len(fruits)>2:
    fruits.pop()
    print(fruits)