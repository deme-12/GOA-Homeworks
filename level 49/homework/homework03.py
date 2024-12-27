def only_duplicates(st):
    unique_list = ""
    for i in st:
        if st.count(i) > 1:
            unique_list += i
    return unique_list