
def valid_phone_number(phone):
    # 1. სიგრძე უნდა იყოს ზუსტად 14 
    if len(phone) != 14:
        return False
    
    # 2. ტექსტი უნდა იწყებოდეს ( და მთავრდებოდეს )
    if phone[0] != '(' or phone[4] != ')':
        return False
    
    # 3. 5 ინდექსზე  უნდა იყოს სფეისი 
    if phone[5] != ' ':
        return False
    
    # 4. 9 ინდექსზე უნდა იყოს  " - "
    if phone[9] != '-':
        return False
    
    # 5.  ვამოწმებთ რიცხვებ

    if not (phone[1:4].isdigit() and phone[6:9].isdigit() and phone[10:].isdigit()):
        return False
    
    # თუ ყველა წესს აკმაყოფილებს, ვაბრუნებთ True
    return True






def valid_phone_number(phone):
    # სიგრძის შემოწმება
    if len(phone) != 14:
        return False
    
    # სიმბოლოების  შემოწმება
    if phone[0] != '(' or phone[4] != ')' or phone[5] != ' ' or phone[9] != '-':
        return False
    
    # რიცხვების შემოწმება
    if not (phone[1:4].isdigit() and phone[6:9].isdigit() and phone[10:].isdigit()):
        return False

    return True

