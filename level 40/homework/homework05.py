def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    first_letter = alphabet.find(chars[0])
    last_letter = alphabet.find(chars[-1])

    for letters in alphabet [first_letter: last_letter]:
        if letters not in chars:
            return letters
