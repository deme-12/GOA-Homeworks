# 1) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი

numb = [10,15,20,35,35,323,111,222,231,155,444]
the_biggest_numb = numb[0]
for num in numb:
    if the_biggest_numb < num:
        the_biggest_numb = num
print(the_biggest_numb)
        