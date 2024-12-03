# 4) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას

def sentence(s):
    lst = s.split()
    return "-".join(lst)

print(sentence("ada    adasd    sdaasda      asdasada"))