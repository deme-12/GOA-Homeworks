def to_camel_case(text):
    text = text.replace("_","-")
    text = text.split("-")
    result = ""
    for words in text:
        if text.index(words) == 0:
            result += words
        else:
            result += words.capitalize()
         
    return result