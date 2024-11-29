# 9) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია

def names(lst):
    N_names = []
    for name in lst:
        if name[0] == "N":
            N_names.append(name)
    print(N_names)

names(["Nodar","sandro","temo","Nino"])