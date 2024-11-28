# 6) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
symbols = ["a","b","c","d","e","a","c","e","n"]
new_symbols = []
for num in symbols:
    if symbols not in new_symbols: # თუ სიმბოლო ჯერ არ არის ახალ სიაში
        new_symbols.append(symbols)
print(new_symbols)