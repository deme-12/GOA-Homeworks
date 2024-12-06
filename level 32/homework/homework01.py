def find_short(s):
    lst = s.split()
    shortest_word = lst[0]
    for words in lst:
        if len(shortest_word) > len(words):
            shortest_word = words
    return len(shortest_word)













