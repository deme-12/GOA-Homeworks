# 6) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ

def numbers(lst,lst2):
    sum1 = 0
    for num in lst:
        sum1 += num
    sum2 = 0
    for num in lst2:
        sum2 += num
    print(sum1 * sum2)

numbers([2,2,2,2,2],[10,20,30,40])   

