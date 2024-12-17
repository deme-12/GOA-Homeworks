
# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.



def high(x):
    words = x.split() # x - გავხლიჩეთ და გადავაქციეთ სიად

    max_score = 0   #  ცვლადი სადაც შევინახავთ სიტყვის ქულების რაოდენობას
    max_word = ""   # ცვლდადი სადაც შეინახება ყველაზე მეტი ქულის მქონე სიტყვა ( დავაბრუნებთ ბოლოს)

    for word in words: # გადაუარეთ სიას სადაც თითოეულ სიტყვას ვაკონტროლებთ word ცვლადით

        # score - ში გამოვითვლით თვითოეული სიტყვის ქულას
        score = sum(ord(letters) -96 for letters in word) 
        # 1. `for letter in word`: გადაუვლის თითოეულ ასოს სიტყვაში.
        # 2. `ord(letters)`: იღებს კოდს სიმბოლოსთვის (მაგალითად, 'a' = 97, 'b' = 98).
        # 3. `ord(letters) - 96`: თითოეულ ასოს გარდაქმნის ანბანიის პოზიციად (მაგ., 'a' = 1, 'b' = 2,  'z' = 26).
        # 4. `sum(): აჯამებს სიტყვაში ყველა ასოს ქულას.


        if score > max_score:  # თუ ამ სიტყვას (word) აქვს მეტი ქულა, ვიდრე აქამდე ნაპოვნი მაქსიმალური ქულა:
            max_score = score  # განვაახლებთ `max_score-ს (ახალი მაქსიმალური ქულით).
            max_word = word  # `max_word`- განვაახლებთ და  შევინახავთ ამ ახალ სიტყვას.

    return max_word  # ფუნქცია აბრუნებს იმ სიტყვას, რომელსაც ყველაზე მეტი ქულა აქვს.



def high(x):
    splited_x = x.split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    result = ""
    max_score = 0
    
    for i in splited_x:
        score_sum = 0
        
        for x in i:
            score_sum += alphabet.index(x) + 1
        if score_sum > max_score:
            result = i
            max_score = score_sum
    return result


