# 3) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს string-ს. ამ ფუნქციამ უნდა გაიგოს გადმოცემულ string-ში თითოეული სიმბოლოს რაოდენობა და ჩაამატოს ახალ სიაში(ერთი სიმბოლის რაოდენობა მხოლოდ ერთხელ უნდა ჩაამატოთ. მგალითად თუ string-ში 5 "a" გვხვდება, რიცხვი 5 მასივში მხოლოდ ერთხელ უნდა ჩავამატოთ, მაგრამ სხვა სიმბოლოც თუ გვხვდება იგივე რაოდენობით, მას ვამატებთ ჩვეულებრივ). საბოლოდ დაასორტირეთ მიღებული სია ზრდადობით და დააბრუნეთ

def chars_count(str):
    no_dublicates = []
    result = []
    for chars in str:
        if chars not in no_dublicates:
            no_dublicates.append(chars)
    for chars in no_dublicates:
        result.append(str.count(chars))
    return sorted(result)
print(chars_count("gggooa"))