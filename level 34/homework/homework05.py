# 5) შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვების სიას და აბრუნებს მას კლებადობის მიხედვით დასორტირებულს

def numbers(lst):
    return sorted(lst)[::-1]
print(numbers([8,5,4,3,8,1,3,2,4,7]))