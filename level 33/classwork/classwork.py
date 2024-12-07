# convert string to camel case

def to_camel_case(text):
    text = text.replace("_","-")
    splited_str = text.splited("-")

    for i in range(1,len(splited_str)):
        splited_str[i] = splited_str[i].capitalize()
    return"".join(splited_str)