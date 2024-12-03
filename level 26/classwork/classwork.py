# lower

# name = "nika"
# user_name = input("please enter your name ").lower()

# print(name == user_name)

# upper

# text = "hello my name is nika"
# upper_text = text.upper()
# print(text)
# print(upper_text)


def upper_and_lower(text):
    upper_index = 1

    result = ""
    
    for i in text:
        if upper_index == 3:
            result += i.upper()
            upper_index = 1
        else:
            result += i.lower()
        upper_index += 1
    return result

print("hello my name is nika")