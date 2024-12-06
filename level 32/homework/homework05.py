def longest(a1, a2):
    new_string = a1 + a2
    result = ""
    for letters in new_string:
        if letters not in result:
            result += letters
    return "".join(sorted(result))