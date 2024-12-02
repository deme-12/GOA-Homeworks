def spin_words(sentence):
    new_list = []
    sentence = sentence.split(" ")
    for words in sentence:
        if len(words) >= 5:
            new_list.append(words[::-1])
        else:
            new_list.append(words)
            
    return " ".join(new_list)