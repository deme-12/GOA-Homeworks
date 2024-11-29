# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი

def  remove_first_and_last_elements(lst):
    print(lst[1:-1])
remove_first_and_last_elements(["a","ee","dd","32","dsfs","dsd"])