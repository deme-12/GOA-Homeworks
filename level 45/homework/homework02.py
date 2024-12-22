
def is_int_array(arr):
    if not isinstance(arr,list) # თუ arr არ არის სია დაბრუნდეს False
        return False
    if len(arr) == 0: # თუ სია არის ცარიელი დაბრუნდეს True
        return True
    for element in arr: # გადაუვლით ლუპით მასივს
        # თუ ელემენტი არ იქნება ინტეჯერი ან ათწილადი დააბრუნებს False ასევე თუ ინთეჯერი არ უდრის 
        if not isinstance(element(int,float) or (isinstance(element,float) and element != int(element))):
            return False
    return True


element = 5.5
print(isinstance(element, float))  # True (რადგან 5.5 არის float)
print(element != int(element))  # True (რადგან 5.5 != 5)
# მთლიანობაში: True

element = 5.0
print(isinstance(element, float))  # True (რადგან 5.0 არის float)
print(element != int(element))  # False (რადგან 5.0 == 5)
# მთლიანობაში: False

element = 5
print(isinstance(element, float))  # False (რადგან 5 არის int)
print(element != int(element))  # არ მოწმდება (რადგან isinstance დაბრუნდა False)
# მთლიანობაში: False