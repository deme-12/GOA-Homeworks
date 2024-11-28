# 3) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი

numb = [100,200,15,166,340,55,776,323]
the_smallests_numb = numb[0]
for num in numb:
    if the_smallests_numb > num:
        the_smallests_numb = num
print(the_smallests_numb)