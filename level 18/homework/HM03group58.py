# # 3) შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე
names = ("jame","alice","maria","alan","george")
for name in names:
    if name.startswith("A") or name.startswith("a"):
        print(name)