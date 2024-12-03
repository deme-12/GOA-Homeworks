# 2) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)
def sentence(s):
    lst = s.split(" ")
    for words in lst:
        print(len(words))
sentence("deme mamauladze")
