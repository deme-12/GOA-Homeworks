# 5) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა მარტივ რიცხვს

numb = int(input("enter number: "))
for num in range(1,numb):
    counter = 0
    for num2 in range(1,numb +1):
        if num % num2 == 0:
            counter += 1
    if counter == 2:
        print(num)


    