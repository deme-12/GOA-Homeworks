def dublicates(string):
    result = []
    for word in string: # გადაუაროთ სიას
        new_word = ""  # შევქმენით ცვლადი გადავეცით ცარიელი სთრინგი
        for i in range(len(word)): #სთრინგის თითოეულ სიმბოლოს გადაუვლით
            # თუ i == 0 ნიშნავს რომ პირველი ემემენტია და უნდა ჩაემატოს, შემდეგ ხდება შედარება თუ მომდევნო ასე არ არის წინა ასოს ტოლი, ნიშნავს რომ არის უნიკალური და ჩაემატება სიაში. 
            if i == 0 or word[i] != word[i-1]: 
                new_word += word[i]
        result.append(new_word)
    return result


