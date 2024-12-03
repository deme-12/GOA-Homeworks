def is_isogram(string):
    string = string.lower()
    for letters in string:
        if string.count(letters) > 1:
            return False
    return True