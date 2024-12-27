def in_asc_order(arr):
    sorted_list = arr.copy()
    sorted_list.sort()
    
    for i in range(len(arr)):
        if sorted_list[i] != arr[i]:
            return False
    
    return True



def valid_braces(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    
    return s == "" 



def expanded_form(num):
    str_num = str(num)
    result = []
    
    for i in range(len(str_num)):
        if str_num[i] != "0":
            result.append(str_num[i] + "0" * (len(str_num) - 1 - i))
    
    return " + ".join(result) 


