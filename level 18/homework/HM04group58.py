# 4) შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი, რომლებიც არ მეორდება სიაში

numb = [1,2,4,6,5,1,43,56,2,87,43]
unique_sum = 0
for num in numb:
    if numb.count(num) == 1:  # თუ რიცხვი ხდება მხოლოდ ერთხელ სიაში  numb.count(num) == 1:
        unique_sum += num  # ეს რიცხვი დავამატოთ ჯამში
print(unique_sum)

#count() მეთოდი გვაძლევს, რამდენჯერ გვხვდება კონკრეტული რიცხვი სიაში 
# თუ რიცხვი სიაში მხოლოდ ერთხელაა, მაშინ მისი დუბლიკატი არ არსებობს, და ასეთ რიცხვებს დავამატებთ ჯამში.
