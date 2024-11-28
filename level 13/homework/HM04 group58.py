# 4) შექმენით სია შემდგარი 10 ელემენტისგან. დაპრინტეთ ის და მომხარებელს შემოატანინეთ რიცხვი 1-დან 10-ჩათვლით. შემდეგ წაშალეთ სიის ის ელემენტი რომელი რიცხვიც გადმოგეცათ და დაპრინტეთ განახლებული სია

names = ["gio","temo","zura","aleko","sophia","vano","tamari","iza","vakho","nino"]

num = int(input("enter number from 1 to 10" ))
names.pop(num -1)
print(names)