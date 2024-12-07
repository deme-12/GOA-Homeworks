def remove_url_anchor(url):
    new_str = ""
    for char in url:
        if char == "#":
            break
        else:
            new_str += char
    return new_str
        