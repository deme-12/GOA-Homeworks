# 1) შექმენით ფუნქცია manual_pop, რომელსაც გადაეცემა ორი არგუმენტი, სია და ინდექსი. წაშალეთ სიიდან, გადმოცემულ ინდექსზე მყოფი ელემენტი. საბოლოოდ კი დააბრუნეთ ეს სია(არ გამოიყენოთ .pop ფუნქცია)

def manual_pop(numbers,index):
    result = []
    index1 = 0
    for i in numbers:
        if index1 != index:
            result.append(i)
        index += 1
    return result
print(manual_pop([22,50,60], -1))


# 2) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ რიგით მერამდენეა ის.

symbol ="Hello"
index = 0
for i in symbol:    
    print(i + " - " + str(index))
    index += 1


#  2) შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. ამ ფუნქციამ უნდა შეართოს ეს სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი

def manual_list(str_list,string1):
    result = ""

    for i in str_list:
        result += i + string1
    return result[:-3]

print(manual_list(list("python") ," - "))



# 3) შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ან სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ. დააბრუნეთ მიღებული შედეგი.

def manual_count(lst,element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

print(manual_count("hello world","l"))


